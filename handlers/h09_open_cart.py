from aiogram import F, Bot, Router
from aiogram.types import CallbackQuery, Message

from database.utils import db_get_cart_items
from keyboards.inline import cart_actions_kb

router = Router()


@router.message(F.text == "🛒 Корзина")
async def handle_cart(message: Message):
    """Показ товаров в корзине - reply"""
    chat_id = message.chat.id
    await show_cart(chat_id=chat_id, send_fn=message.answer)


@router.callback_query(F.data == 'Корзина заказа')
async def open_cart(callback: CallbackQuery):
    '''Обработка инлайн кнопки корзина заказа'''
    chat_id = callback.from_user.id
    await show_cart(chat_id=chat_id, send_fn=callback.message.answer)


async def show_cart(chat_id: int, send_fn):
    "Показ содержимого корзины"
    cart_items = db_get_cart_items(chat_id) #TODO Реализовать функцию для db

    if not cart_items:
        await send_fn("Ваша корзина пуста! Добавьте товары в нее.")
        return

    text = "Содержание вашей корзины 🧺:\n"
    total = 0

    for item in cart_items:
        total = float(item["final_price"]) + total
        text += f"{item["product_name"]} - {item["quantity"]}шт. - {total}₽"

    text += f"\nИтоговая сумма: {total}₽"
    await send_fn(text, reply_markup=cart_actions_kb())