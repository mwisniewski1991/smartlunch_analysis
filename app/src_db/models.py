from sqlalchemy import Column, Integer, String, ForeignKey, Float

def create_Restaurants(base):
    class Restaurants(base):
        __tablename__ = 'Restaurants'
        id = Column('id', Integer, primary_key=True)
        name = Column('name', String(100))

        def __init__(self, id, name) -> None:
            self.id = id
            self.name = name

    return Restaurants

def create_Restaurants_rates(base):
    class Restaurants_rates(base):
        __tablename__ = 'Restaurants_rates'
        id = Column('id', String(20), primary_key=True) #{restaurant_id}_{yyyymmdd}
        id_restaurants = Column('id_restaurants', ForeignKey('Restaurants.id'))
        rate_date = Column('rate_date', String(8)) #yyyymmdd
        rate =  Column('rate', Float(2))
        rates_count = Column('rates_count', Integer)

        def __init__(self, id:str, id_restaurants:int, rate_date:str, rate:float, rates_count:int) -> None:
            '''
            Args:
                id: {id_restaurants}_{rate_date} 
                id_restaurants: restaurant if from main table
                rate_date: yyyymmdd - day when rate has bee checked,
                rate: float user rate,
                rates_count: integer how many people rate
            '''
            self.id = id
            self.id_restaurants = id_restaurants
            self.rate_date = rate_date
            self.rate = rate
            self.rates_count = rates_count
    return Restaurants_rates
     
def create_Scrap_plan(base):
    class Scrap_plan(base):
        __tablename__ = 'Scrap_plan'
        id = Column('id', String(50), primary_key=True) #{yyyymmdd}_{place_id}_{order_date}_{menu_id}
        place_id = Column('place_id', Integer)
        scrap_day = Column('scrap_day', String(8))
        order_date = Column('order_date', String(8))
        menu_id = Column('menu_id', Integer)
        restaurant_id = Column('restaurant_id', Integer, ForeignKey('Restaurants.id'))

        def __init__(self, id:str, place_id:int, scrap_day:str, order_date:str, restaurant_id:int, menu_id:int) -> None:
            self.id = id
            self.place_id = place_id
            self.scrap_day = scrap_day
            self.order_date = order_date
            self.restaurant_id = restaurant_id
            self.menu_id = menu_id

    return Scrap_plan


def create_Menus(base):
    class Menus(base):
        __tablename__ = 'Menus'
        id = Column('id', String(50), primary_key=True) #{menu_id}_{place_id}_{scrap_datetime}_{meal_id}
        menu_id = Column('menu_id', Integer)
        place_id = Column('place_id', Integer)
        scrap_datetime = Column('scrap_day', String(13)) #yyyymmdd_hhmm
        order_date = Column('order_day', String(8)) #yyyymmdd
        meal_id = Column('meal_id', Integer, ForeignKey('Meals.id'))
        mean_name_pl = Column('mean_name_pl', String(100))
        total_price = Column('total_price', Integer)
        is_vege = Column('is_vege', Integer) #bool
        is_cold = Column('is_cold', Integer) #bool
        avg_rate = Column('avg_rate', Float)
        rates_count = Column('rates_count', Integer)
        dishes_left = Column('dishes_left', Integer)
        
        def __init__(self, id:int, menu_id:int, place_id:int,
                     scrap_datetime:str, order_date:str,
                     meal_id:int, mean_name_pl:str, total_price:int, is_vege:int, is_cold:int, 
                     avg_rate:float, rates_count:int, dishes_left:int) -> None:
            self.id = id 
            self.menu_id = menu_id
            self.place_id = place_id
            self.scrap_datetime = scrap_datetime
            self.order_date = order_date
            self.meal_id = meal_id
            self.mean_name_pl = mean_name_pl
            self.total_price = total_price
            self.is_vege = is_vege
            self.is_cold = is_cold
            self.avg_rate = avg_rate
            self.rates_count = rates_count
            self.dishes_left = dishes_left  
    
    return Menus

def create_Meals(base):
    class Meals(base):
        __tablename__ = 'Meals'
        id = Column('id', Integer, primary_key=True)
        name_pl = Column('name', String(100))

        def __init__(self, id:int, name_pl:str) -> None:
            self.id = id
            self.name_pl = name_pl
    
    return Meals