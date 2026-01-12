from aiogram.utils.keyboard import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def start_keyboard():
    """Кнопка старт"""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Начать 😄")]],
        resize_keyboard=True
    )
