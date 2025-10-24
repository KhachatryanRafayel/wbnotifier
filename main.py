from aiogram import Bot, Dispatcher, types
from time import time
import asyncio

from price_manager_class import price_manager
from orders_manager_class import orders_manager
from stock_manager_class import stock_manager
from config import TG_TOKEN

API_TOKEN = TG_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
chat_id = None

pm = price_manager() 
om = orders_manager()
sm = stock_manager()

buttons = [
    '🆕 Orders (FBS)', 
    '💵 Price of My Goods',
    '📦 Number of goods in stock',
]

last_request_time = {
    '🆕 Orders (FBS)': 0,
    '💵 Price of My Goods': 0, 
    '📦 Number of goods in stock': 0
}

cached_responses = {
    '🆕 Orders (FBS)': None,
    '💵 Price of My Goods': None,
    '📦 Number of goods in stock': None
}

CACHE_DURATION = 10

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text=btn)] for btn in buttons],
    resize_keyboard=True
)

@dp.message()
async def handle_all_messages(message: types.Message):
    global chat_id, last_request_time, cached_responses
    chat_id = message.chat.id
    text = message.text

    if text not in buttons:
        await message.answer('Use one of navigation buttons 👇', reply_markup=keyboard)
        return

    current_time = time()
    needs_refresh = (
        current_time - last_request_time[text] >= CACHE_DURATION or 
        cached_responses[text] is None
    )

    if not needs_refresh:
        await message.answer(cached_responses[text])
        return

    last_request_time[text] = current_time

    if text == '🆕 Orders (FBS)':
        if not om.is_there_any_order():
            response = '🟨 You don\'t have any new orders yet. 🤗'
        else:
            response = om.get_orders_text()

    elif text == '💵 Price of My Goods':
        response = pm.get_price_text()

    elif text == '📦 Number of goods in stock':
        response = sm.get_remaining_text()

    cached_responses[text] = response
    await message.answer(response)

async def scheduled_task():
    if pm.is_price_changed():
        message = pm.get_price_change_text()
        await bot.send_message(chat_id, message)
        message = pm.get_price_text()
        await bot.send_message(chat_id, message)
    if pm.is_secondary_price_lower_official_price():
        message = pm.get_secondary_price_lower_official_price_text()
        await bot.send_message(chat_id, message)
    if om.is_there_new_order():
        message = om.get_orders_text()
        await bot.send_message(chat_id, message)
    if not sm.is_remaining_products():
        message = sm.get_no_remaining_text()
        await bot.send_message(chat_id, message)
    else:
        print("Noting is changed...")

async def periodic_check():
    while True:
        await asyncio.sleep(300)  # 5 minutes
        try:
            await scheduled_task()
        except Exception as e:
            print(f"Error in scheduled task: {e}")

async def on_startup():
    asyncio.create_task(periodic_check())

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())