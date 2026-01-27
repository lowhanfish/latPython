
a = [2,3,4]

def multiply():
    a.append(9)

print("sebelum fungsi dipanggil", a)
multiply()
print("dan setelah fungsi dipanggil", a)


def tambahDataBaru (data) :
    data.append(12)

tambahDataBaru(a)
print("setelah di tambahkan data baru", a)

def jumlahkanData(data):
    for index,item in enumerate(data):
        a = item+3
        data[index]= a

jumlahkanData(a)
print("setelah data di jumlahkan dengan 3", a)
