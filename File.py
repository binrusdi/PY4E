# Untuk bekerja dengan file di python kita mempunyai fungsi open()
# fungsi open() mengambil dua parameter
# open("namaFile", "mode")
# fungsi open() mengembalikan objek file
# Mode pada fungsi open( q)

# "r", baca -> membuka file untuk dibaca, jika tidak ada error
# "a", tambahkan -> membuka file untuk ditambahkan, membuat file jika tidak ada
# "w", menulis -> membuka file untuk ditulis, membuat file jika tidak ada, menimpa isi file yg ada
# "x", buat -> membuat file yg ditentukan, mengembalikan kesalahan jika file tsb ada

# Penanganan file
# "t", untuk teks
# "b", untuk binner (misalnya gambar)
f = open("file.txt", "rt")
# "rt" adalah mode baca dan teks
print(f)

# Metode pada fungsi open()
# read(), mengembalikan semua isi teks file
print(f.read())

# readline(), mengembalikan satu baris teks pada file
print(f.readline())

# write(), untuk menulis ke dalam file
f.write()

# close(), untuk menutup file
f.close()
