player = input("Our contestant's name is: ")
print(f'\nWelcome {player} to Who Wants to Be a Millionaire!')

print('\nHere is your first question:')
print('What is the capital of France?')
print('A: Berlin')
print('B: Madrid')
print('C: Paris')
print('D: Rome')
answer = input('Your answer is (A B C D): ')
if answer.lower() == 'c':
    print('Right! You won $100')
else:
    print('You are wrong. The correct answer is C: Paris. You lost the game.')
    print('Game Over!')
    exit()

print('\n2nd Question gives you $200')
print('Which planet is known as the Red Planet?')
print('A: Earth')
print('B: Mars')
print('C: Neptune')
print('D: Sun')
answer = input('Your answer is (A B C D): ')
if answer.lower() == 'b':
    print('Congratulations! You won $200')
else:
    print('You are wrong. The correct answer is B: Mars. You lost the game.')
    print('Game Over!')
    exit()

print('\n3rd Question gives you $300')
print('What is the largest mammal in the world?')
print('A: Elephant')
print('B: Blue Whale')
print('C: Giraffe')
print('D: Great White Shark')
answer = input('Your answer is (A B C D): ')
if answer.lower() == 'b':
    print('Congrats! You won $300')
else:
    print('You are wrong. The correct answer is B: Blue Whale. You lost the game.')
    print('Game Over!')
    exit()

print('\nYou have won a total of $600')
print('Next question is for $1 million!')
print('What is the chemical symbol for gold?')
print('A: Au')
print('B: Ag')
print('C: Gd')
print('D: Og')
answer = input('Your answer is (A B C D): ')
if answer.lower() == 'a':
    print( f'🎉 Congratulations!!! {player} You are now a MILLIONAIRE!!! 🎉')
else:
    print('You are wrong. The correct answer is A: Au. You lost the game.')
    print('Game Over!')
    exit()

print('\nNow you are rich enough to buy a mansion and a Lamborghini!')
print('Thank you for playing Who Wants to Be a Millionaire!')
print('Have a great day!')
