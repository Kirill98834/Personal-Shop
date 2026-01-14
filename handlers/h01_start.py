from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart

from database.utils import db_register_user
from handlers.h02_get_contact import show_main_menu
from keyboards.reply import start_keyboard, phone_button

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    """Обработка команды старт"""
    photo = FSInputFile("media/welcome.jpg")
    await message.answer_photo(
        photo=photo,
        caption=f"Добрый день, <i>{message.from_user.full_name}</i>\nНажмите кнопку ниже, чтобы начать",
        parse_mode='HTML',
        reply_markup=start_keyboard()
    )


@router.message(F.text == "Начать 😄")
async def handle_start_button(message: Message):
    """Обработчик кнопки начать"""
    await handle_start(message)


async def handle_start(message: Message):
    """Продолжение обработки кнопки начать и добавление регистрации нового пользователя"""
    await register_user(message)


async def register_user(message: Message):
    """регистрация пользователя, показ гл.меню, запись логов о регистрации"""
    chat_id = message.chat.id
    full_name = message.from_user.full_name


    if db_register_user(full_name, chat_id):

        await message.answer(text=f'Добро пожаловать')
        await show_main_menu(message)
    else:
        await message.answer(
            text='Для связи нужен Ваш контактный номер',
            reply_markup=phone_button()
        )
