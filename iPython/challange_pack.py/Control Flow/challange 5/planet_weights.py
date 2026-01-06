# Yerda vazningizni kiriting
earth_weight = float(input("Enter your weight on Earth (kg): "))

# Sayyorani tanlash
planet = int(input("Enter the planet number (1-7): "))

# Kerakli joyni hisoblash
if planet == 1:
    destination_weight = earth_weight * 0.38
    print("Your weight on Mercury is", destination_weight, "kg")
elif planet == 2:
    destination_weight = earth_weight * 0.91
    print("Your weight on Venus is", destination_weight, "kg")
elif planet == 3:
    destination_weight = earth_weight * 0.38
    print("Your weight on Mars is", destination_weight, "kg")
elif planet == 4:
    destination_weight = earth_weight * 2.53
    print("Your weight on Jupiter is", destination_weight, "kg")
elif planet == 5:
    destination_weight = earth_weight * 1.07
    print("Your weight on Saturn is", destination_weight, "kg")
elif planet == 6:
    destination_weight = earth_weight * 0.89
    print("Your weight on Uranus is", destination_weight, "kg")
elif planet == 7:
    destination_weight = earth_weight * 1.14
    print("Your weight on Neptune is", destination_weight, "kg")
else:
    print("Invalid planet number")