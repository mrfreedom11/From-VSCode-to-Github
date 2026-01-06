import math

def main():
    while True:
        print("\n==================")
        print("Area Calculator 📐")
        print("==================")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")

        choice = input("\nWhich shape: ")

        if choice == "1":
            base = float(input('Base: '))
            height = float(input('Height: '))
            area = (height * base) / 2
            print(f"\nThe area of triangle is {area}")

        elif choice == "2":
            length = float(input('Length: '))
            width = float(input('Width: '))
            area = length * width
            print(f'\nThe area of rectangle is {area}')

        elif choice == "3":
            side = float(input('Side: '))
            area = side ** 2
            print(f'\nThe area of square is {area}')

        elif choice == "4":
            radius = float(input("Radius: "))
            area = math.pi * (radius ** 2)
            print(f"\nThe area of circle is {area}")

        else:
            print("Invalid choice, please select a valid option.")

# Funksiyani chaqirish
main()
