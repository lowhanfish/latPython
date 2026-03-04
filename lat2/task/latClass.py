class Tester:
    def __init__(self , data):
        self.nama = "Kiken"
        self.alamat = "Jalan Beringin"
        self.datax= data

    def n_nama(self):
        return f"Hy Saya {self.nama} dan usia saya adalah {self.datax['age']}"
    
    def l_alamat(self):
        return f"Alamat saya di {self.alamat}"
    

datax =  {
    "job": "Programmer",
    "age" : 40
}

test = Tester(datax)  # Memberikan argumen datax ke konstruktor

nama = test.n_nama()
alamat = test.l_alamat()


print(nama)
print(alamat)
