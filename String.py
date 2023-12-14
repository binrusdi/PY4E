# cetak sting literal dengan fungsi print()
print('Ini string literal, yang digunakan langsung pada fungsi print()')

# Tetapkan string ke variable
string = 'String ini di tetapkan dalam variable \'string\''
print(string) # String ini di tetapkan dalam variable 'string'

# String adalah Array
# Tanda siku dapat menakses elemen string
word = 'Hello world!'
print(word[1]) # e

# Perulangan melalui string
for chr in word:
    print(chr, end=' ') # H e l l o   w o r l d !

# Periksa panjang string
word_length = len(word)
print('\n', word_length) # 12

# Periksa frasa/char dalam string
text = 'saya adalah manusia'
print('manusia' in text) # True
print('manusia' not in text) # False
