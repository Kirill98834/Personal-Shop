from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery
from pyexpat.errors import messages

from keyboards.inline import show_product_by_category

router = Router()

@router.callback_query(F.data.reqexp(r"^category_(\d+$"))
async def show_product(callback: CallbackQuery):
     '''Показ всех продуктов из выбранной категории'''
     chat_id = callback.message.chat_id
     message_id = callback.message.message_id
     category_id = int(callback.data.split('_')[-1])
     try:
         await callback.bot.edit_message_text(
             text='выберите продукт',
             message_id=message_id,
             chat_id=chat_id,
             reply_markup=show_product_by_category(category_id)
         )
     except TelegramBadRequest:
         await  callback.answer('Не удалось открыть выбранную категорию')
