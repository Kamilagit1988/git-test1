from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7541077124:AAGPDfJ-eyaXNPpySZi3w9tcbR3Ye3P6jcQ"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
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
    await message.answer("Введите опцию:", reply_markup= inline_kb)


@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")


@dp.callback_query_handler(text = 'calories')
async def get_formulas(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
   await state.update_data(age = message.text)
   data = await state.get_data()
   await message.answer(f"Введите свой рост.")
   await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
   await state.update_data(growth = message.text)
   data = await state.get_data()
   await message.answer(f"Введите свой вес.")
   await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = (10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])+5)
    await message.answer(f'Ваша норма калорий: {result} ккал в сутки (для мужчин)')
    await UserState.weight.set()
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
