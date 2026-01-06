ph = int(input('Enter a pH level (0-14): '))
if ph >= 14:
    print("toxic")
elif ph <= 7:
    print("neutral")
elif ph >= 0:
    print("acid")
else:
    print("wrong number")