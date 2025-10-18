import datetime
now = datetime.datetime.now()
print(now)

# Mengembalikan tahun dan tanggal
print(now.year) # tahun
# strdtime('format') <- memformat objek tanggal menjadi string yg dpt dibaca
print(now.strftime('%A')) # Hari(english)
print(now.strftime('%a')) # Hari disingkat
print(now.strftime('%w')) # Hari dalam angka, 0 (sunday)
print(now.strftime('%d')) # Hari dalam satu bulan/tanggal angka
print(now.strftime('%b')) # Bulan disingkat
print(now.strftime('%B')) # Bulan
print(now.strftime('%m')) # Bulan dalam angka
print(now.strftime('%y')) # Tahun tanpa abad
print(now.strftime('%Y')) # Tahun
print(now.strftime('%H')) # 24 jam
print(now.strftime('%I')) # 12 jam
print(now.strftime('%p')) # Am/Pm
print(now.strftime('%M')) # Menit
print(now.strftime('%S')) # Detik
print(now.strftime('%f')) # Microdetik
print(now.strftime('%Z')) # Zona waktu
print(now.strftime('%W')) # Nomer minggu dalam setahun
print(now.strftime('%c')) # Tanggal dan waktu lokal
print(now.strftime('%C')) # Abad
print(now.strftime('%x')) # Tanggal lokal
print(now.strftime('%X')) # Waktu lokal
print(now.strftime('%G')) # ISO Tahun
print(now.strftime('%u')) # ISO Minggu
print(now.strftime('%V')) # ISO nomer minggu