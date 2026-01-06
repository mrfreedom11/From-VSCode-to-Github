def kda(k, d, a):
    # 0 bilan bo'lishdan qochish
    if d == 0:
        return (k + a)  # Ba'zi o'yinlarda o'limlar 0 bo'lsa, faqat k+a hisoblanadi
    return (k + a) / d

# misol uchun:
print(kda(10, 2, 5))   # chiquvchi
