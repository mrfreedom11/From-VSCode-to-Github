menu = {
    1: "🍔 Cheeseburger",
    2: "🍟 Fries",
    3: "🥤 Soda",
    4: "🍦 Ice Cream",
    5: "🍪 Cookie"
}


def get_item(number):
    return menu.get(number, "❌ Sorry, that item is not on the menu.")


def welcome():
    print("\n========================================")
    print(" 🍔 Welcome to McDonald's Drive-Thru! 🍟")
    print("========================================")
    for number, item in menu.items():
        print(f"{number}) {item}")
    print("0) 🚪 Exit")

def main():
    while True:
        welcome()
        try:
            choice = int(input("\nWhat would you like to order? Enter item number: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if choice == 0:
            print("\n👋 Thanks for visiting! Enjoy your meal!")
            break
        else:
            print(f"\n✅ You ordered: {get_item(choice)}\n")

if __name__ == "__main__":
    main()
