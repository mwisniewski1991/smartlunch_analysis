from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src_db import models, db_manager, files_reader
from src_db.config import DB_DIR, DB_NAME, DB_ENGINE

Base = declarative_base()
engine = create_engine(f'{DB_ENGINE}:///{DB_DIR}/{DB_NAME}')
Session = sessionmaker(bind=engine)

Restaurants = models.create_Restaurants(Base)
Restaurants_rates = models.create_Restaurants_rates(Base)
Scrap_plan = models.create_Scrap_plan(Base)

def main() -> None:
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = Session()

    scrap_plan_raw_data:list = files_reader.import_all_scrap_plan_data()

    for scrap_plan in scrap_plan_raw_data:
        scrap_day = scrap_plan.get('scrap_date')
        scrap_data = scrap_plan.get('data')

        for place_id in scrap_data.keys():
            days_list:list =  scrap_data[place_id]

            for order_day in days_list:
                order_day_text = list(order_day.keys())[0]
                order_day_text = order_day_text.replace('-', '') #replace "-" for standarization dates in DB

                for menu in list(*order_day.values()):
                    menu_id:int = menu.get('menu_id')
                    restaurant_id = menu.get('place_id')
                    scrap_plan_id = f'{scrap_day}_{place_id}_{order_day_text}_{menu_id}'

                    db_manager.add_scrap_plan(session, Scrap_plan, scrap_plan_id, (scrap_plan_id, place_id, scrap_day, order_day_text, restaurant_id, menu_id))


    session.close()

if __name__ == '__main__':
    main()