# Regex ialah rangkaian karakter yg membentuk pola pencarian
# Regex digunakan untuk memeriksa, apakah suatu string berisi pola pencarian yg ditentukan
import re
# contoh
# Apakah suatu steing di mulai dan diakhiri oleh kata yg ditentukan
txt = "The rain in spain"
result_txt = re.search("^The.*spain$", txt)
if result_txt:
    print(
        f"The di urutan {len(txt)-len(txt)} dan spain di index ke {len(txt)-5}")
else:
    print("tidak cocok")

# Fungsi pada Regex
# findall <- Mengembalikan List yg berisi semua kecocokan
# search <- Mengembalikan objek yg cocok jika ada kecocokan di manapun dalam string
# split <- Mengembalikan list yang stringnya telah dipisahkan pada setiap kecocokan
# sub <- Mengganti satu atau banyak kecocokan dengan string

# Metakarakter ialah karakter dengan arti khusus
# [] <- mencari/menampilkan seperangkat karakter
kurung_siku = re.findall("[c-m]", txt)
print(kurung_siku)

# garis miring terbalik <- memberi sinyal untuk urutan khusus
teks_garing = "disini ada angka 75"
garing = re.findall("\d", teks_garing)
print(garing)  # ['7', '5']

# . <- Mencari karakter apapun, kecuali garis baru
teks_titik = "kamu sangat cantik"
titik = re.findall("ca..ik", teks_titik)
print(titik)
