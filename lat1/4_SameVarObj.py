"""

Apabila suatu variable ditugaskan dalam variabel lain, kedua variabel akan merujuk pada objek
yang sama. untuk mengetahui bahwa variabel tersebut merujuk pada objek yang sama, kita bisa menggunakan
id(), karena setiap objek punya identitas uniq

"""

print("========= SEBELUM ========")
mukamu = "jelek"
mukaku = "ganteng"

print("id mukamu : ", id(mukamu))
print("id mukaku : ", id(mukaku))

print("========= SESUDAH ========")
mukamu = mukaku
print("id mukamu : ", id(mukamu))
print("id mukaku : ", id(mukaku))