# Sintaks untuk bertukar data
# Json adalah teks yang ditulis dengan notasi objek Js
import json
# Menguraikan json, hasilnya menjadi dict
objek_js = '{ "name": "jhon", "age": 30, "city": "New York"}'
konvert_dict = json.loads(objek_js)
print(konvert_dict['age'])
print(type(konvert_dict))

# Konversi dari Objek/dict python ke json
# gunakan parameter indent=nomor di metode dumps, untuk lekukan json
# Gunakan separators=",", ".", ":" parameter untuk mengubah pemisah 
dict_py = {"name": "Rusdi", "age": 30, "city": "Cimahi"}
json_parse = json.dumps(dict_py)
print(json_parse, type(json_parse))


