import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
MINI_APP_URL = os.getenv("MINI_APP_URL")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    webapp_button = KeyboardButton(
        text="🚀 Открыть приложение",
        web_app=WebAppInfo(url=MINI_APP_URL)
    )

    main_keyboard = ReplyKeyboardMarkup(
        keyboard=[[webapp_button]],
        resize_keyboard=True,
        is_persistent=True,
        input_field_placeholder="Нажмите кнопку 👇"
    )

    await message.answer(
        "Привет! Для работы с сервисом используйте наше мини-приложение.",
        reply_markup=main_keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())