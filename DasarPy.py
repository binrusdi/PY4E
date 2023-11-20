""" Dasar Python """
''' Operator Aritmatika '''
print(f"\n''' Oerator Aritmatika '''")
# ** eksponen
print(f"Ekponen\n 3 ** 5 = {3 ** 5}")

# % modulus
print(f"Modulus\n 20 % 2 = {20 % 2}")

# // pembagian bilangan bulat
print(f"Pembagian bilangan bulat\n 5 // 2 = {5 // 2} ")

# / Divisi
print(f"Divisi\n 5 / 2 = {5 / 2}")

# * Perkalian
print(f"Perkalian\n 3 * 3 = {3 * 3}")

# - Penegurangan
print(f"Pengurangan\n 7 - 3 = {7 - 3}")

# + Penambahan
print(f"Penambahan\n 9 + 1 = {9 + 1}")

''' Operator penugasan yang ditambah '''
print(f"\n'''Operator penugasan yang ditambah'''")
print(f"var += 1 sama dengan var = var + 1")
print(f"var -= 1 sama dengan var = var - 1")
print(f"var *= 1 sama dengan var = var * 1")
print(f"var /= 1 sama dengan var = var / 1")
print(f"var %= 1 sama dengan var = var % 1")

''' Operator Walrus '''
print(f"\n''' Opertor Walrus '''")
print('''Operator Walrus mengizinkan penetapan variable dalam ekspresi,
sambil mengembalikan nilai variable''')
print(f"myvar := \"Hello, world!\"")
print(myvar := "Hello, world!")

''' Kata kunci sep= '''
print("\n'''Kata kunci sep='''")
print("Menentukan cara memisahkan object jika lebih dari satu seperti:\nprint('Masuk', 'Pergi', 'Keluar')")
print('Masuk', 'Pergi', 'Keluar', sep=",")

''' Kata kunci end= '''
print("\n'''Kata Kunci end='''")
print("""
Argument 'end' digunakan untuk menghindari garis baru ketika output
""")
print("""pharse = ['printed', 'with', 'a', 'dash']""")
print(""" for word in pharse:
              print(word, end='-') """)
pharse = ['printed', 'with', 'a', 'dash']
for word in pharse:
    print(word, end='-')