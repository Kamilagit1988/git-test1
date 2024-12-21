from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = InlineKeyboardMarkup(
    button = [

        [
            InlineKeyboardButton(text = 'Расчитать норму калорий', callback_data= 'calories')
            InlineKeyboardButton(text = 'Формулы расчета', callback_data= 'formulas')
        ]

    ]
)



start_menu = ReplyKeyboardMarkup(
    keyboard= [

        [
            KeyboardButton(text='Расчитать'),
            KeyboardButton(text='Информация')
        ]

    ], resize_keyboard = True
)

@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup= start_menu)


@dp.message_handler(text = 'Расчитать')
async def main_menu(message):
    await message.answer("Введите опцию:", reply_markup= kb)
    await UserState.menu.set()

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await call.message()

@dp.callback_query_handler(text = 'calories')
async def get_formulas(call):
    await call.message.answer("Введите опцию.")
    await call.message()

#@dp.callback_query_handler(text = 'info')
#async def infor(call):
#    await call.message.answer("Информация о боте")
#    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
