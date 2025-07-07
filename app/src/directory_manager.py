from pathlib import Path
import json
import datetime

def create_log_directory_log() -> str:
    pass

def create_directory(dir:str, year:int, month:int, day:int) -> str:
    '''
    Create directories in structre for year, month and day if not exists.
    Return string for created path.

    Args:
        dir: path when directories will be created,
        year: year number for which directory will be created,
        month: year number for which directory will be created,
        day: year number for which directory will be created,
    '''
    path_dir:Path = Path(f'{dir}')
    if not path_dir.exists():
        path_dir.mkdir()

    path_year: Path = Path(f'{dir}/{year}')
    if not path_year.exists():
        path_year.mkdir()

    path_month: Path = Path(f'{dir}/{year}/{month}')
    if not path_month.exists():
        path_month.mkdir()

    path_day: Path = Path(f'{dir}/{year}/{month}/{day}')
    if not path_day.exists():
        path_day.mkdir()
    
    return str(path_day)

def save_restaurants_menu(data:dict, dir:str, place_id:int, menu_id:int, scrap_time:str, delivery_date:str) -> None:
    file_name:str = f'{place_id}_{menu_id}_{scrap_time}_{delivery_date}.json'
    with open(f'{dir}/{file_name}', 'w') as file:
        data_text = json.dumps(data)
        file.write(data_text)

def save_scrap_plan(data:dict, dir:str, scrap_date:str) -> None:
    file_name:str = f'{scrap_date}.json'
    with open(f'{dir}/{file_name}', 'w') as file:
        data_text:str = json.dumps(data)
        file.write(data_text)

def save_restaurant(data:dict, dir:str, restaurant_id:str) -> None:
    file_name:str = f'{restaurant_id}.json'
    with open(f'{dir}/{file_name}', 'w') as file:
        data_text:str = json.dumps(data)
        file.write(data_text)

def read_scrap_plan(dir:str, year:int, month:int, day:int, date_to_find:str) -> dict:
    '''
    Based on dir anc date function read scrap plan.
    Args:
        dir: directoryfor scrap plan
        data_to_find: date which will be searching for
    Return: dict
    '''
    try:
        dir_to_open:str = f'{dir}/{year}/{month}/{day}/{date_to_find}.json'
        with open(dir_to_open) as file:
            data:dict = json.load(file)
        return data
    except FileNotFoundError:
        return {'error':'FileNotFoundError - scrap plan does not exists for this day.'}