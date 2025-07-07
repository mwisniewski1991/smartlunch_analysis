from pathlib import Path
from .config import DATA_DIRECTORY
import json
from datetime import datetime

RESTAURANTS_DIR = DATA_DIRECTORY.get('restaurants')
SCRAP_PLAN_DIR = DATA_DIRECTORY.get('scrap_plan')
MENUS_DIR = DATA_DIRECTORY.get('menus')

def import_all_files(dir) -> list:
    '''
    Return all paths to files with restaurants data
    '''
    files:Path.glob = Path(dir).glob('**/*')
    return [obj for obj in files if obj.is_file()]
    

def import_all_restaurants_data() -> list:
    '''
    Return list with all scraped restaurants dicts.
    '''
    restaurants_list:list = []
    files_list:list = import_all_files(RESTAURANTS_DIR)

    for file in files_list:
        _, _, year, month, day, _ = file.parts
        file_date = datetime(int(year), int(month), int(day))

        with open(file, 'r') as file_text:
            data = json.load(file_text)
        
        data['rate_date'] = file_date.strftime('%Y%m%d')
        restaurants_list.append(data)

    return restaurants_list

def import_all_scrap_plan_data() -> list:
    '''
    Read all scrap plan data. In return dict join scrap day from file and scrap_data.
    '''
    scrap_plan_list:list = []
    files_list:list = import_all_files(SCRAP_PLAN_DIR)

    for file in files_list:
        _, _, year, month, day, _ = file.parts
        file_date = datetime(int(year), int(month), int(day))

        with open(file, 'r') as file_text:
            data = json.load(file_text)

        scrap_plan_list.append({'scrap_date':file_date.strftime('%Y%m%d'), 'data': data})
    
    return scrap_plan_list

def import_all_menus_data() -> list:
    '''
    Return dictionary and files name for all menus data
    '''
    return import_all_files(MENUS_DIR)