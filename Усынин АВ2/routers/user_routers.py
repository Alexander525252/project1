from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from web_app.main_web_app import markup

user_router = Router()


@user_router.message(CommandStart())
async def command_google_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@user_router.message(Command("google"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Start", reply_markup=markup)

@user_router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")