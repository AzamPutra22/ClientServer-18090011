import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="kampus")
c = db.cursor()
sql = "INSERT INTO Mahasiswa(NIM,Nama,Alamat) VALUES (%s, %s, %s)"
val = ("011", "Azam Putra Imanto", "Pemalang")
c.execute(sql, val)

#commit untuk apply perubahan data
db.commit()

c.close()