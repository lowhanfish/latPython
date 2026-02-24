# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.leg = 4

#     def speak(self, says):
#         print(f"{self.name} Says : {says}")

# my_dog = Dog("BullDog")
# another_dog = Dog("PitBull")

# print(my_dog.speak("Grrrrr"))
# print(another_dog.speak("Guk Guk"))

class Profile:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
        self.riwayat_pendidikan = []
        self.riwayat_jabatan = []

    def tambah_pendidikan(self, jenjang, universitas, thn):
        data = {
            "jenjang" : jenjang, "universitas" : universitas, "thn" : thn 
        }
        self.riwayat_pendidikan.append(data)
        # print(f"Pendidikan {jenjang} untuk {self.nama} berhasil ditambahkan.")

    def tampilkan_riwayat(self):
        print(f"--- Profil Pegawai -----")
        print(f"Nama : {self.nama}")
        print("--------------------")
        print(f"Nip : {self.nip}")
        print("--------------------")
        
        if self.riwayat_pendidikan:
            for i, data in enumerate(self.riwayat_pendidikan):
                print (f"{data['universitas']}")
                print("--------------------")


profile = Profile("Kiken", "0201012")
profile.tambah_pendidikan("S1", "STMIK BINA MANGSA", 2004)
profile.tambah_pendidikan("S2", "UNIVERSITAS ISLAM SULTAN AGUNG", 2014)
profile.tambah_pendidikan("S3", "MIT University", 2027)
profile.tampilkan_riwayat()