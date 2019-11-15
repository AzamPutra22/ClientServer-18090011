import json

data = '[{ "nama" : "Azam", "alamat" : "Pemalang" },' \
       '{ "nama" : "Putra", "alamat" : "Pelutan"}]'

result = json.loads(data)

for x in result:
    print(x['nama'])