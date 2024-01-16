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
# search <- Mengembalikan objek Match jika ada kecocokan di manapun dalam string
# split <- Mengembalikan list yang stringnya telah dipisahkan pada setiap kecocokan
# sub <- Mengganti satu atau banyak kecocokan dengan string

# Metakarakter ialah karakter dengan arti khusus
# [] <-
kurung_siku = re.findall("[c-m]", txt)
print(kurung_siku)
