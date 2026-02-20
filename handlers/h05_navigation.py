from aiogram import F, Router, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, message_id

from handlers.h03_order import make_order

router = Router()

@router.message(F.text =="Назад⬅")
async def return_to_back(message: Message, bot: Bot):
    """Возвращение на шаг назад и удаление каких-либо сообщений"""
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id=message.message_id - 1)
    except TelegramBadRequest:
        pass

    await make_order(message, bot)