import telebot
from datetime import datetime
import time

token = 'put here your token'
bot = telebot.TeleBot(token)
your_id = -000000000

while True:
    day = datetime.today().weekday()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    p1 = now.replace(hour=8, minute=38, second=0, microsecond=0)  # first lesson
    first_class = p1.strftime("%H:%M:%S")

    p2 = now.replace(hour=10, minute=10, second=0, microsecond=0)  #
    second_class = p2.strftime("%H:%M:%S")

    p3 = now.replace(hour=12, minute=00, second=0, microsecond=0)
    third_class = p3.strftime("%H:%M:%S")

    p4 = now.replace(hour=13, minute=40, second=0, microsecond=0)
    fourth_class = p4.strftime("%H:%M:%S")

    p5 = now.replace(hour=15, minute=20, second=0, microsecond=0)
    fifth_class = p5.strftime("%H:%M:%S")

    if day == 0:  # MONDAY

        if current_time == first_class:
            bot.send_message(your_id, "  put smth here")
            time.sleep(1)

        if current_time == second_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == third_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fourth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fifth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

    if day == 1:  # TUESDAY
        if current_time == first_class:
            bot.send_message(your_id, "  put smth here")
            time.sleep(1)

        if current_time == second_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == third_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fourth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fifth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

    if day == 2:  # WEDNESDAY
        if current_time == first_class:
            bot.send_message(your_id, "  put smth here")
            time.sleep(1)

        if current_time == second_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == third_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fourth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fifth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

    if day == 3:  # THURSDAY
        if current_time == first_class:
            bot.send_message(your_id, "  put smth here")
            time.sleep(1)

        if current_time == second_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == third_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fourth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fifth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

    if day == 4:  # FRIDAY

        if current_time == first_class:
            bot.send_message(your_id, "  put smth here")
            time.sleep(1)

        if current_time == second_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == third_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fourth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)

        if current_time == fifth_class:
            bot.send_message(your_id, " put smth here")
            time.sleep(1)
