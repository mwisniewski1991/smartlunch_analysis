HOUR_TIME_FORMAT:str = '%Y%m%d_%H%M'
DATE_FORMAT:str = '%Y%m%d'

DATA_DIRECTORY:dict = {
    'menus': 'data/menus',
    'restaurants': 'data/restaurants',
    'scrap_plan': 'data/scrap_plan',       
}

DATES_URL:str = 'https://app.smartlunch.pl/employees/api/v2/delivery_dates?'
MENU_CATEGORIES_URL:str = 'https://app.smartlunch.pl/employees/api/v2/menu_categories'
RESTAURANTS_MENU_URL:str = 'https://app.smartlunch.pl/employees/api/v2/menu_categories/471580/menu_items?delivery_date=2023-01-30&delivery_place_id=1195'

delivery_places = [
    {'id': 1195, 'name': 'CLR'},
    {'id': 1194, 'name': 'CLŁ'},
    {'id': 1203, 'name': 'Biurowiec TME'},
    {'id': 1204, 'name': 'Oddział Gdynia'},
    {'id': 1205, 'name': 'Oddział Kraków'},
]

KEY_FOR_MENU_ITEMS:str = 'menu_items'

KEYS_TO_REMOVE:list[str] = [
'price_after_funding',
'dish_description_uk',
'dish_description_en',
'dish_ingredients',
'dish_allergens',
'name_en',
'name_uk',
'dish_description_pl',
]