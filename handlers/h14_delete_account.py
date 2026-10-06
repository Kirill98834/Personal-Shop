from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from config import MANAGER_ID
from database.utils import db_delete_user_by_telegram_id
from keyboards.inline import delete_confirm_kb, get_settings_menu
from keyboards.reply import start_keyboard

router = Router()

@router.callback_query(F.data == "delete_account")
async def handle_delete_account(callback: CallbackQuery):
    '''Запрос на удаление аккаунта'''
    await callback.message.edit_text("Вы уверены, что хотите удалить аккаунт?\nДанные будут удалены",
                                     reply_markup=delete_confirm_kb())

@router.callback_query(F.data == "confirm_delete")
async def handle_confirm_delete(callback: CallbackQuery, bot: Bot):
    '''Подтверждение удаления аккаунта'''
    telegram_id = callback.from_user.id
    full_name = callback.from_user.full_name

    success = db_delete_user_by_telegram_id(telegram_id)

    if success:
        try:
            await callback.message.delete()
        except TelegramBadRequest:
            pass

        await callback.message.answer(text = "Ваш аккаунт удален. Для повторной работы необходимо зарегистрироваться."
                                      , reply_markup=start_keyboard())
        await bot.send_message(MANAGER_ID, f"Пользователь {full_name} удалил аккаунт ({telegram_id})")
    else:
        await callback.message.edit_text("Ошибка удаления аккаунта.", reply_markup=get_settings_menu())