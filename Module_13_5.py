from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text = 'Информация', callback_data= 'info')
kb.add(button)

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
    await message.answer("Рады вас видеть!", reply_markup= start_menu)
@dp.message_handler(text = 'Расчитать')
async def set_age(message):
    await message.answer("Введите свой возраст.")
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




#@dp.callback_query_handler(text = 'info')
#async def infor(call):
#    await  call.message.answer("Инфоормация о боте")
#    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)