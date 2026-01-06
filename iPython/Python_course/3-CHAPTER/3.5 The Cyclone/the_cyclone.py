height = int(input('What is your height (cm)? '))
credits = int(input('How many credits do you have? '))
if height > 136 and credits > 9:
  print('Enjoy the ride!');
if height < 137 and credits > 9:
  print('You are not tall enough to ride');
if height > 136 and credits < 10:
  print('You dont have enough credits');
if height < 137 and credits < 10:
  print('you do not have any requirements')

