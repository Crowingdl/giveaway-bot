import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

TOKEN = "7906003165:AAGsFbOdXO3Cn1Xl-rxncJ2CBgpQqBLK9BM"
CHANNEL_ID = "-1002415989494"
ADMIN_ID = 6699586232  # Ganti dengan ID admin

dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

async def is_subscribed(user_id: int) -> bool:
    try:
        chat_member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except TelegramBadRequest:
        return False

@dp.message(Command("start"))
async def start(message: Message):
    if await is_subscribed(message.from_user.id):
        await message.answer("✅ Kamu sudah subscribe! Kamu bisa ikut giveaway.")
    else:
        await message.answer("⚠️ Kamu harus subscribe ke channel @basehah untuk menggunakan bot ini.")

@dp.message(Command("giveaway"))
async def create_giveaway(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("🎉 Giveaway dimulai! Peserta yang sudah subscribe bisa ikut dengan /join")
    else:
        await message.answer("❌ Hanya admin yang bisa membuat giveaway.")

@dp.message(Command("join"))
async def join_giveaway(message: Message):
    if await is_subscribed(message.from_user.id):
        await message.answer("🎟️ Kamu telah bergabung dalam giveaway!")
    else:
        await message.answer("⚠️ Kamu harus subscribe ke channel @basehah untuk ikut serta.")

from aiogram import Bot  # Tambahkan ini!
from aiogram.client.bot import DefaultBotProperties

async def main():
    global bot
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

