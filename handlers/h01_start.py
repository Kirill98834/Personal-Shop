from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from keyboards.reply import start_keyboard

router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    """Обработка команды старт"""
    photo=FSInputFile("media/welcome.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"Добрый день, <i>{message.from_user.full_name}</i>\nНажмите кнопку ниже, чтобы начать",
        parse_mode='HTML',
        reply_markup=start_keyboard()
    )
