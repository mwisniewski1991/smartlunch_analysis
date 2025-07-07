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

def main() -> None:
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = Session()

    restauratns_raw_data:list = files_reader.import_all_restaurants_data()
    for restaurant in restauratns_raw_data:
        id = restaurant.get('place_id')
        name = restaurant.get('name')
        rate_date = restaurant.get('rate_date')
        rate = restaurant.get('rate')
        rates_count = restaurant.get('rates_count')
        rate_id = f'{id}_{rate_date}'

        db_manager.add_restaurant(session, Restaurants, id, (id, name))
        db_manager.add_restaurant_rate(session, Restaurants_rates, rate_id, (rate_id, id, rate_date, rate, rates_count))


    session.close()

if __name__ == '__main__':
    main()