from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src_db import models, db_manager, files_reader
from src_db.config import DB_DIR, DB_NAME, DB_ENGINE
from datetime import datetime
import json

Base = declarative_base()
engine = create_engine(f'{DB_ENGINE}:///{DB_DIR}/{DB_NAME}')
Session = sessionmaker(bind=engine)

Restaurants = models.create_Restaurants(Base)
Restaurants_rates = models.create_Restaurants_rates(Base)
Scrap_plan = models.create_Scrap_plan(Base)
Menus = models.create_Menus(Base)
Meals = models.create_Meals(Base)

def decode_menu_file_name(file_name:str) -> tuple:
    '''
    Decode necesery data from file name:
    Args: 
        file_name: file which will be parsed.
    Return: tuple with place id, menu id, scrap datetime, order date
    '''

    place_id = int(file_name[0:4])
    menu_id = int(file_name[5:11])
    scrap_date_time = file_name[12:25]
    order_date = file_name[26:36].replace('-','')

    return (place_id, menu_id, scrap_date_time, order_date)

def decode_true_false(text_value:str) -> int:
    if text_value == True:
        return 1
    elif text_value == False:
        return 0
    else:
        raise ValueError

def main() -> None:
    '''
    Function scan all files with menus. 
    Add all new menus to DB
    Add all new meals to DB.
    '''
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = Session()

    files_list = files_reader.import_all_menus_data()
    for file in files_list:
        place_id, menu_id, scrap_date_time, order_date = decode_menu_file_name(file.name)

        with open(file, 'r') as file_text:
            menus_list = json.load(file_text).get('menu_items')

        for menu in menus_list:
            meal_id:int = int(menu.get('id'))
            total_price:int = menu.get('total_price')
            is_vege:int = decode_true_false(menu.get('is_vege')) #bool
            is_cold:int = decode_true_false(menu.get('is_cold')) #bool
            avg_rate:float = menu.get('avg_rate')
            rates_count:int = menu.get('rates_count')
            dishes_left:int = menu.get('dishes_left')
            meal_name_pl:str = menu.get('name_pl')
            id:str = f'{menu_id}_{place_id}_{scrap_date_time}_{meal_id}'

            db_manager.add_menu(session, Menus, id, (id, menu_id, place_id, scrap_date_time, order_date, meal_id, meal_name_pl, total_price, is_vege, is_cold, avg_rate, rates_count, dishes_left))
            db_manager.add_meal(session, Meals, meal_id, (meal_id, meal_name_pl))

    session.close()


if __name__ == '__main__':
    main()



