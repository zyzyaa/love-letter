import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")  # https://xxx.pages.dev

dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="Открыть письмо 💌",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])
    await m.answer("У тебя письмо. Откроешь?", reply_markup=kb)

async def main():
    if not BOT_TOKEN or not WEBAPP_URL:
        raise RuntimeError("Нужно задать BOT_TOKEN и WEBAPP_URL в переменных окружения.")
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
