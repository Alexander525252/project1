from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.web_app import WebAppChat

markup = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = "Google" ,
                web_app=WebAppInfo(url="https://translate.google.com/?hl=ru&sl=auto&tl=ru&op=translate")
            )
        ]
    ]
)