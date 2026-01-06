review = int(input('Enter your answer (1-4): '))
if review >= 4.5:
  print('Extraordinary')
elif review >= 4:
  print('Excellent')
elif review >= 3:
  print('Good')
else:
  print('Eh')