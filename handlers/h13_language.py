from aiogram import Router, F
from aiogram.types import CallbackQuery

from database.utils import db_update_language
from keyboards.inline import get_language_keyboard, get_settings_menu

router = Router()

@router.callback_query(F.data == "change_language")
async def change_language(callback:CallbackQuery):
    '''Смена языка'''
    await callback.message.edit_text(text="Сменить язык: ", reply_markup= get_language_keyboard())

@router.callback_query(F.data.startswith("lang"))
async def set_language(callback: CallbackQuery):
    '''Смена языка и сохранение данных в базу данных'''
    new_language = callback.data.split("_")[1]
    telegram_id = callback.from_user.id

    db_update_language(telegram_id, new_language)

    text = "Язык успешно изменен на Русский✅" if new_language == 'ru' else 'Language successfully changed to English✅'
    await callback.message.edit_text(text=text, reply_markup=get_settings_menu())