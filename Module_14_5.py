from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


from crud_functions1 import initiate_db, get_all_products, add_user, is_included


api = ""
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

inline1_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data="product_buying"),
        InlineKeyboardButton(text='Product2', callback_data="product_buying"),
        InlineKeyboardButton(text='Product3', callback_data="product_buying"),
        InlineKeyboardButton(text='Product4', callback_data="product_buying")]
    ]
)

start_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Расчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить'),
            KeyboardButton(text='Регистрация')

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




@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in get_all_products():
        number = i[0]
        title = i[1]
        description = i[2]
        price = i[3]
        with open(f'image/{str(number) + ".png"}', 'rb') as img:
            await message.answer_photo(img, caption=f'Название: {title} | Описание: {description} | Цена: {price}')
    await message.answer('Выберите продукт для покупки: ', reply_markup=inline1_kb)
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()



class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(usnam=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(em=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(ag=message.text)
    data = await state.get_data()
    add_user(data['usnam'], data['em'], data['ag'])
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
