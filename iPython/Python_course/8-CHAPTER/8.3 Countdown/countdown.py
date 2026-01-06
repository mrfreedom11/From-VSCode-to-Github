import random
import datetime
bday_messages = [
    'Hope you have a very Happy Birthday! 🎈',
    "It's your special day - get out there and celebrate! 🎉",
    'You were born and the world got better - everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞'
]

random_message = random.choice(bday_messages)


today = datetime.date.today()
next_birthday = datetime.date(2026, 11, 21)  # 👈 change to your real birthday

days_away = (next_birthday - today).days

if today == next_birthday:
    print(random_message)
else:
    print(f"My next birthday is {days_away} days away!")
