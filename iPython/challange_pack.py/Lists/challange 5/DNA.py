# 1. DNA ro'yhati
dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT',
                'CAT', 'TAT', 'CCC', 'ACG', 'GAA',
                'ACC', 'GGA']

# 2. Qidiriladigan element
item_to_find = 'CAT'

# 3. Boolean o'zgaruvchi, dastlab False
item_found = False

# 4. Ro'yxatdan qidirish
for item in dna_sequence:
    if item == item_to_find:
        item_found = True
        break   # topilgandan keyin siklni to'xtatamiz

# 5. Natijani chiqarish
if item_found:
    print("Item Found!")
else:
    print("Item not found.")
