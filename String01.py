# Mengiris String
word = 'Python'
print(word[0:]) # Python
print(word[0:3]) # Pyt
print(word[:len(word)]) # Python
print(word[-len(word):]) # Python
print(word[-6:]) # Python -> karena urutan akhir string adalah -1

# Memodifikasi string
upper_word = word.upper()
print('Ini method upper() mengganti ke huruf besar ->', upper_word) # PYTHON
lower_word = word.lower()
print('Ini method lower() mengganti ke huruf kecil ->', lower_word)
strip_word = ' python '
result_strip_word = strip_word.strip()
print('Ini method strip() menghapus spasi awal dan akhir ->',result_strip_word)