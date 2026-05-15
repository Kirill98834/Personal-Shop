from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from bot_utils.counting import counting_products
from config import MANAGER_ID
from database.utils import db_get_user_phone

router = Router()

@router.callback_query(F.data == "confirm_order")
async def confirm_order(callback: CallbackQuery, bot: Bot):
    '''Подтверждение заказа'''
    user = callback.from_user
    phone = db_get_user_phone(user.id)
    mention = f'<a href="tg://user?id={user.id}"> {user.full_name} </a>'
    user_text = f'новый заказ от {mention} с номером телефона {phone}'
    context = counting_products()

    if not context:
        await callback.message.edit_text('Заказы отсутствуют')
        await callback.answer()
        return