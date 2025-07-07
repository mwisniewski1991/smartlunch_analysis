import sqlalchemy.orm 
from sqlalchemy.orm import sessionmaker 


def is_existed(session: sqlalchemy.orm.session.Session, model:sqlalchemy.orm.decl_api.DeclarativeMeta, id:int) -> bool:
    '''
    Function return information if id exists in database.
    Args: 
        session: sqlalchemy.orm.session.Session
        model: database model/table
        id: id to checked in database
    Return: bool 
        Information if id exist in database
    '''
    result =  session.query(model).filter(model.id == id).scalar()
    if result:
        return True
    return False

def add_restaurant(session: sqlalchemy.orm.session.Session, model:sqlalchemy.orm.decl_api.DeclarativeMeta, values_id:int, values:tuple) -> None:
    if not is_existed(session, model, values_id):
        restaurant = model(*values)
        session.add(restaurant)
        session.commit()

def add_restaurant_rate(session: sqlalchemy.orm.session.Session, model:sqlalchemy.orm.decl_api.DeclarativeMeta, values_id:int, values:tuple) -> None:
    if not is_existed(session, model, values_id):
        rate = model(*values)
        session.add(rate)
        session.commit()

def add_scrap_plan(session: sqlalchemy.orm.session.Session, model:sqlalchemy.orm.decl_api.DeclarativeMeta, values_id:int, values:tuple) -> None:
    if not is_existed(session, model, values_id):
        scrap_plan = model(*values)
        session.add(scrap_plan)
        session.commit()
    
def add_menu(session: sqlalchemy.orm.session.Session, model:sqlalchemy.orm.decl_api.DeclarativeMeta, values_id:int, values:tuple) -> None:
    if not is_existed(session, model, values_id):
        menu = model(*values)
        session.add(menu)
        session.commit()

def add_meal(session: sqlalchemy.orm.session.Session, model:sqlalchemy.orm.decl_api.DeclarativeMeta, values_id:int, values:tuple) -> None:
     if not is_existed(session, model, values_id):
        meal = model(*values)
        session.add(meal)
        session.commit()