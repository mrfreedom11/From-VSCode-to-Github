password = input("Parolni kiriting: ")

has_digit = any(c.isdigit() for c in password)
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
length_ok = len(password) >= 8

needs = []  # nimalar kerakligini ro'yxati

if not has_digit:
    needs.append("Raqam yetishmayabdi")

if not has_lower:
    needs.append("Kichik harf yetishmayabdi")

if not has_upper:
    needs.append("Katta harf yetishmayabdi")

if not length_ok:
    needs.append("Parol 8 ta belgidan kam")

if not needs:
    print("Parol yetarlicha kuchli!")
else:
    print("Parol kuchli emas, quyidagilar kerak:")

for n in needs:
        print("-", n)
   
