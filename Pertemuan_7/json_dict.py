import json

mahasiswa = []

Azam = {"nama" : "Azam", "alamat" : "Pelutan"}
Putra = {"nama" : "Putra", "alamat" : "Pemalang"}
Imanto = {"nama" : "Imanto", "alamat" : "Pelutan-Pemalang"}

mahasiswa.append(Azam)
mahasiswa.append(Putra)
mahasiswa.append(Imanto)

json_str = json.dumps(mahasiswa)
print(json_str)