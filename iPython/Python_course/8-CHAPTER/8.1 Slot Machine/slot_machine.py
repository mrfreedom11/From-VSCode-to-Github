# Write code below 💖
import random
symbols = ('🍒' , ' 🍇', '🍉', '7️⃣')
result = random.choices(symbols , k = 3)
print(' | ' .join(result))
if result.count('7️⃣'):
  print( "Jackpot! 💰")
else:
  print('Thanks for playing')
while True:
  again = input("Play again? (Y/N):").strip().lower()
  if again != 'Y' :
    print('Thanks for playing')
