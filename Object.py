# Sebuah objek/class mempunyai property dan method nya
class Person:
  # fungsi init dipanggil otomatis setiap kali kelas digunakan untuk membuat obj baru
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # mengontrol apa yg hars dikembalikan
  # ketika obj kelas di representasikan sbg string
  def __str__(self):
    return f'{self.name} {self.age}'
  # Ini sdalah metode dalam objek
  def salam (self, status):
    print(f'selamat malam {self.name}, sang {status}')
    
p1 = Person('jhon', 36)
print(p1.name) # mencetak properti dr class
print(p1.age)  # mencetak properti dr class
print(p1) # fungsi __str__ akan berfungsi disini
p1.name = 'marsya'
p1.salam('duda') # mencetak metode dr class

# Kelas anak yang mewarisi prop dan metode kelas induk
# kirimkan class induk sbg parameter kelas anak
# class Student(Person):
class Student(Person):
  def __init__(self, name, age, year):
  # super() yang akan membuat kelas anak mewarisi prop dan metode induk
    super().__init__(name, age)
    # menambahkan prop dikelas anak
    # value prop harus berupa variable yang diteruskan melalui parameter init
    self.gradution_year = year
  # ini adalah metode
  def salam(self):
    print('selamat datang', self.name, 'ditahun ajaran', self.gradution_year)
siswa = Student('Ihsan', 2, 2022)
print(siswa.gradution_year)
siswa.salam()