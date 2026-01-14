from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select, DECIMAL, join, func
from sqlalchemy.exc import IntegrityError

from database.base import engine
from database.models import (Users, Categories, Products, Carts,
                             FinallyCarts, Orders)


def get_session():
    """Подключение сессии к bd"""
    return Session(engine)


def db_register_user(full_name, chat_id):
    """регистрация юзера в дб"""
    try:
        with get_session() as session:
            query = Users(name=full_name, telegram=chat_id)
            session.add(query)
            session.commit()
        return False
    except IntegrityError:
        return True


def db_update_user(chat_id, phone: str):
    """номер телефона юзера, номера строкового типа"""
    with get_session() as session:
        query = update(Users).where(Users.telegram == chat_id).values(phone=phone)
        session.execute(query)
        session.commit()


def db_create_user_cart(chat_id):
    """создание корзины юзера, ограничение: 1 юзер=1 корзина"""
    try:
        with get_session() as session:
            subquery = session.scalar(select(Users).where(Users.telegram == chat_id))
            query = Carts(user_id=subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False
    except AttributeError:
        return False
