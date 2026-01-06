import random

# 1. Ro'yhat yaratamiz
my_numbers = []
winning_numbers = []
# 2. 1 dan 69 gacha random 5 ta son tanlaymiz
for i in range(5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))
# 3. 1 dan 26 gacha random bitta son tanlaymiz
my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))
# 4. Natijani chiqaramiz
print("Mening raqamlarim: ", my_numbers)
print("Yutgan raqamlar: ", winning_numbers)
# 5. Tekshiramiz
if my_numbers == winning_numbers:
  print('Siz yutdingiz') # Teng bo'lsa yutiqni chiqazadi
else:
    print('Siz yutqazdingiz') # Teng bo'lmasa yutqazganini chiqazadi
