from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.filters.state import State, StatesGroup
from loader import dp, bot
import yaml


with open('texts.yml', 'r', encoding='utf-8') as file:
    txt_messages = yaml.safe_load(file)


@dp.message(CommandStart())
async def msg_start(message: types.Message):
    await message.answer(txt_messages['greeting'])
    await message.answer(txt_messages['howToUse'])
