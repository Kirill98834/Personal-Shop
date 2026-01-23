from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile

from keyboards.inline import generate_category_menu
from keyboards.reply import back_to_main_menu

router=Router()

@router.message(F.text == "✅ Сделать заказ")
async def make_order(message: Message, bot: Bot):
    """Обработка кнопки оформить заказ с дальнейшим переходом в категории товаров"""
    chat_id = message.chat.id
    await  bot.send_message(chat_id, "Формируем заказ...", reply_markup=back_to_main_menu())
    await message.answer(text="Выберите категорию", reply_markup=generate_category_menu(chat_id))