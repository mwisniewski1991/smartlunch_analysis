from requests import Session
from src.config import DATES_URL, MENU_CATEGORIES_URL, KEY_FOR_MENU_ITEMS, KEYS_TO_REMOVE



def get_dates(session:Session, place_id:int) -> dict:
    user_params:dict = {
        'delivery_place_id': place_id,
    }
    response:Session.Response = session.get(DATES_URL, params=user_params)
    try:    
        result:dict = response.json()
        return result
    except ValueError:
        return {'error_message':'Error during parsing JSON with dates.'}

def get_restaurants(session:Session, place_id:int, day:str, hour:str) -> list:
    '''
    Return restaurants id which are availabe on specific time for specific.

    Args:
        session: Request.session object.
        place_id: id for searcing places
        day: format yyyy-mm-dd
        hour: format HH:MM 
    '''
    user_params:dict = {
        'day': day,
        'hour': hour,
        'delivery_place_id': place_id,
    }
    response:Session.Response = session.get(MENU_CATEGORIES_URL, params=user_params)
    try:    
        result:dict = response.json()
        return result
    except ValueError:
        return {'error_message':'Error during parsing JSON with dates.'}

def get_restaurants_menu(session:Session, place_id:int, menu_id:int, day:str) -> dict:
    '''
    Return restaurant menu

    Args:
        session: Request.session object.
        place_id: id for searcing places
        restaurant_id: restaurant id 
        day: format yyyy-mm-dd
    '''
    user_params:dict = {
        'delivery_date': day,
        'delivery_place_id': place_id,
    }
    URL:str = f'{MENU_CATEGORIES_URL}/{menu_id}/menu_items'
    response:Session.Response = session.get(URL, params=user_params)
    try:    
        result:dict = response.json()
        return parse_restaurants_menu(result) 
        
    except ValueError:
        return {'error_message':'Error during parsing JSON with dates.'}

def parse_restaurants_menu(data:dict) -> dict:
    '''
    Function remove keys from restaurant menu.
    Args:
        data: dict object with restaurant menu.
    Return:
        dictionary without not required item.
    '''
    for menu in data.get(KEY_FOR_MENU_ITEMS):
        for key in KEYS_TO_REMOVE:
            menu.pop(key)
    return data