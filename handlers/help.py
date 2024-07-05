from aiogram import types
from aiogram.filters import Command
from loader import dp, get_user


@dp.message(Command('help'))
async def show_help(message: types.Message):
    user = await get_user(message)
    if user.status == "left":
        commands_list = (
            "Доступные команды:\n"
            "\n"
            "/schedule - <b>Расписание брони</b>\n"
        )
        await message.answer(commands_list, parse_mode='html')
    else:
        commands_list = (
            "Доступные команды:\n"
            "\n"
            "/help - <b>Получить помощь</b>\n"
            "/book - <b>Забронировать аудиторию</b>\n"
            "/schedule - <b>Расписание брони</b>\n"
            "/change - <b>Изменить руководителя</b>"
        )
        await message.answer(commands_list, parse_mode='html')
