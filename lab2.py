from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import asyncio
import random

TOKEN = "7802161506:AAHSCTmhWh4HBr-NKnkcEiIn_2Yn1uXVuCw"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Определяем состояния FSM
class GameState(StatesGroup):
    waiting_for_guess = State()


# Команда /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Это игра 'Угадай число'. Напиши /game, чтобы начать!")


# Команда /game - начало игры
@dp.message(Command("game"))
async def start_game(message: Message, state: FSMContext):
    number = random.randint(1, 100)  # Загадываем число
    await state.update_data(secret_number=number)  # Сохраняем загаданное число
    await state.set_state(GameState.waiting_for_guess)  # Устанавливаем состояние
    await message.answer("Я загадал число от 1 до 100. Попробуй угадать!")


# Обработка ответа пользователя
@dp.message(GameState.waiting_for_guess)
async def process_guess(message: Message, state: FSMContext):
    user_data = await state.get_data()  # Получаем сохранённые данные
    secret_number = user_data["secret_number"]  # Загаданное число

    try:
        guess = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введи число!")
        return

    if guess < secret_number:
        await message.answer("Больше!")
    elif guess > secret_number:
        await message.answer("Меньше!")
    else:
        await message.answer("Поздравляю! Ты угадал 🎉")
        await state.clear()  # Очищаем состояние (игра завершена)


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
