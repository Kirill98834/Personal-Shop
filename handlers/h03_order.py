from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, FSInputFile

from database.utils import db_get_last_orders
from handlers.h02_get_contact import show_main_menu
from keyboards.inline import generate_category_menu
from keyboards.reply import back_to_main_menu

router = Router()


@router.message(F.text == "✅ Сделать заказ")
async def make_order(message: Message, bot):
    """Обработка кнопки оформить заказ с дальнейшим переходом в категории товаров"""
    chat_id = message.chat.id
    await  bot.send_message(chat_id=chat_id, text="Формируем заказ...", reply_markup=back_to_main_menu())
    await message.answer(text="Выберите категорию", reply_markup=generate_category_menu(chat_id))


@router.message(F.text == "📒 История")
async def order_history(message: Message):
    """Демонстрация 10 последних заказов"""
    chat_id = message.chat.id
    orders = db_get_last_orders(chat_id)
    if not orders:
        await message.answer("У вас нет заказов")
        return

    text = "Последние 5 заказов📋:\n\n"
    for item in orders:
        order = item["order"]

        line_price = float(order.final_price)
        text += f"{order.product_name} - {order.quantity}шт. - {line_price} руб. \n\n"
    await message.answer(text)


@router.message(F.text == "Главное меню")
async def handle_main_menu(message: Message, bot: Bot):
    """Обработка кнопки Главное меню и удаление предыдущего сообщения"""
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    except TelegramBadRequest:
        pass
    await show_main_menu(message)

