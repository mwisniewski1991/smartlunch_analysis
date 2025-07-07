from requests import Session
import json
import time
from datetime import datetime
from src.auth import login, password
from src.config import delivery_places, HOUR_TIME_FORMAT,DATE_FORMAT, DATA_DIRECTORY
from src import scraper, directory_manager
from src_bot import telegram_bot

SCRAP_TIME:datetime = datetime.utcnow()
SCRAP_TIME_TEXT:str = SCRAP_TIME.strftime(HOUR_TIME_FORMAT)
SCRAP_DATE_TEXT:str = SCRAP_TIME.strftime(DATE_FORMAT)
SCRAP_PLAN_DIRECTORY:str = DATA_DIRECTORY.get('scrap_plan')
MENUS_DIRECTORY:str = DATA_DIRECTORY.get('menus')

class ScrapPlanLack(Exception):
    def __init__(self,message="Scrap Plan does not exists.") -> None:
        self.message = message
        super().__init__(self.message)



def main() -> None:
    

    scrap_plan:dict = directory_manager.read_scrap_plan(SCRAP_PLAN_DIRECTORY, SCRAP_TIME.year, SCRAP_TIME.month, SCRAP_TIME.day, SCRAP_DATE_TEXT)

    error:str = scrap_plan.get('error', None)
    
    if error:
        # SEND TELEGRAM
        raise ScrapPlanLack
    
    menus_dir:str = directory_manager.create_directory(MENUS_DIRECTORY, SCRAP_TIME.year, SCRAP_TIME.month, SCRAP_TIME.day)
    session = Session()
    session.auth = (login, password)

    for place_id in scrap_plan.keys():
        days_list:list =  scrap_plan[place_id]

        for day in days_list:
            day_text = list(day.keys())[0]

            for menu in list(*day.values()):
                menu_id:int = menu.get('menu_id') 

                menu_object:dict = scraper.get_restaurants_menu(session, place_id, menu_id, day_text)
                directory_manager.save_restaurants_menu(menu_object, menus_dir, place_id, menu_id, SCRAP_TIME_TEXT, day_text)
            
            time.sleep(2)
        time.sleep(3)

    session.close()
    telegram_bot.send_message("Scraping menu finished.")

if __name__ == '__main__':
    main()