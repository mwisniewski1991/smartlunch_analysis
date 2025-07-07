from requests import Session
import json
import time
from datetime import datetime
from src.auth import login, password
from src.config import delivery_places, HOUR_TIME_FORMAT, DATE_FORMAT, DATA_DIRECTORY
from src import scraper, directory_manager
from src_bot import telegram_bot

SCRAP_TIME:datetime = datetime.utcnow()
SCRAP_TIME_TEXT:str = SCRAP_TIME.strftime(HOUR_TIME_FORMAT)
SCRAP_DATE_TEXT:str = SCRAP_TIME.strftime(DATE_FORMAT)
SCRAP_PLAN_DIRECTORY:str = DATA_DIRECTORY.get('scrap_plan')
RESTAURANTS_DIRECTORY:str = DATA_DIRECTORY.get('restaurants')


def add_new_restaurants(current_restaurants:list, new_restaurants:list) -> list:
    '''
    Add new restaurant only if id not exist in current list. Restaurant in scrap_plan format: {restaurant_id, bool}
    Args:
        current_restaurants: ids list of already scraped restaurants 
        new_restaurants: restaurant which will be check for adding.
    '''

    current_ids = [restaurant['place_id'] for restaurant in current_restaurants]

    for new_restaurant in new_restaurants:
        new_id = new_restaurant['place_id']

        if not new_id in current_ids:
            current_restaurants.append(new_restaurant)

    return current_restaurants
    
def parse_restaurants_for_scrap_plan(restaurants: list) -> list:
    '''
    Scrap plan requires restaurant id and bool value False.
    Scrap_plan format: {restaurant_id, bool}

    Args:
        restaurants: list of restaurants for place
    '''
    return [{ 'menu_id':restaurant['id'], 'place_id':restaurant['place_id']} for restaurant in restaurants]

def create_day_hour_matrix(data:list[dict]) -> list[tuple[str]]:
    day_hour_matrix:list = []

    for day in data.get('delivery_dates'):
        day_text = day.get('day').get('date')

        for hour in day.get('hours'):
            hour_text = hour.get('time')

            day_hour_matrix.append((day_text, hour_text))

    return day_hour_matrix

def restaurant_already_saved(restaurant:dict, current_saved_restaurants:list) -> bool:
    restaurant_id = restaurant.get('place_id')
    return restaurant_id in current_saved_restaurants
        

def main() -> None:

    scrap_plan_dir:str = directory_manager.create_directory(SCRAP_PLAN_DIRECTORY, SCRAP_TIME.year, SCRAP_TIME.month, SCRAP_TIME.day)
    scrap_plan:dict = {}
    restaurants_dir:str = directory_manager.create_directory(RESTAURANTS_DIRECTORY, SCRAP_TIME.year, SCRAP_TIME.month, SCRAP_TIME.day)

    session = Session()
    session.auth = (login, password)

    for place in delivery_places:
        place_id = place.get('id')
        
        print(place_id)

        place_dates:dict = scraper.get_dates(session, place_id)

        error_message:str = place_dates.get('error_message', None)
        error_message:str = place_dates.get('error', None)
        if error_message:
            # IN FUTURE SEND MESSAGE BY TELEGRAM
            print(error_message)
            session.close()
            break

        day_hour_matrix:list = create_day_hour_matrix(place_dates)

        scrap_plan_days:list = []

        previous_day_text:str = ''
        scrap_plan_restaurants:list = []
        saved_restaurants_id:list = []

        for day_hour in day_hour_matrix:
            day_text, hour_text = day_hour

            if previous_day_text != day_text and previous_day_text != '' : 
                scrap_plan_days.append({previous_day_text: scrap_plan_restaurants})
                scrap_plan_restaurants = []
            
            restaurants:list =  scraper.get_restaurants(session, place_id, day_text, hour_text)
            restaurants_ids:list =  parse_restaurants_for_scrap_plan(restaurants)
            add_new_restaurants(scrap_plan_restaurants, restaurants_ids)
            previous_day_text = day_text


            #SAVE NEW RESTAURANT
            for restaurant in restaurants:
                if not restaurant_already_saved(restaurant, saved_restaurants_id):
                    restaurant_id = restaurant.get('place_id')
                    saved_restaurants_id.append(restaurant_id)
                    directory_manager.save_restaurant(restaurant, restaurants_dir, restaurant_id)

            time.sleep(2)

        scrap_plan[place_id] = scrap_plan_days
        
        time.sleep(3)

    directory_manager.save_scrap_plan(scrap_plan, scrap_plan_dir, SCRAP_DATE_TEXT)

    session.close()
    telegram_bot.send_message('Scraping restaurants finished.')


if __name__ == '__main__':
    main()