from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def start_keyboard():
    """Кнопка старт"""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Начать 😄")]],
        resize_keyboard=True
    )


def phone_button():
    """Кнопка для получения телефонного номера"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="Введите номер телефона", request_contact=True)
    return builder.as_markup(resize_keyboard=True)


def get_main_menu():
    """формирование кнопок меню"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="✅ Сделать заказ")
    builder.button(text="📒 История")
    builder.button(text="🛒 Корзина")
    builder.button(text="⚙️ Настройки")
    builder.adjust(1, 3)
    return builder.as_markup(resize_keyboard=True)
