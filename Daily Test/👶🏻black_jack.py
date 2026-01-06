import random

print("Salom baby o'yinchi")
print("Xush kelibsiz Black Jack o'yiniga!")

while True:
    random_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    user_cards = []
    computer_cards = []

    user_cards.append(random.choice(random_cards))
    user_cards.append(random.choice(random_cards))
    computer_cards.append(random.choice(random_cards))
    computer_cards.append(random.choice(random_cards))
    
    print(f"\nYour cards {user_cards}, sum: {sum(user_cards)}")
    print(f"Computer's one card is visible: {computer_cards[0]}")

    while sum(user_cards) < 21:
        choice = input('Do you want to take another card (yes/no):').lower()
        if choice == 'yes':
            user_cards.append(random.choice(random_cards))
            print(f"Your cards: {user_cards}, sum: {sum(user_cards)}")
            computer_cards.append(random.choice(random_cards))
            print("Computer also took a card.")

    if sum(user_cards) > 21:
        print("You lost!")
        print("Computer wins!")
    elif sum(user_cards) > sum(computer_cards):
        print("You won!")
        print("Computer lost!")
    elif sum(user_cards) < sum(computer_cards):
        print("Computer won!")
        print("You lost!")
    else:
        print("Draw!")

    print(f"Your cards: {user_cards}, Computer's cards: {computer_cards}")

    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        continue
    else:
        print("Game over. Thank you for playing!")
        break
