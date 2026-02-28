
data1 = list(range(50))
# print("data awal : ", data1)

filtering = [ data for data in data1 if data%2==0]
# print(f"Filtering", filtering)

condition = [f"{data}=Genap" if data%2==0 else f"{data}=Ganjil" for data in data1]
# print(f"Filtering", condition)

nama = "Hy, nama saya adalah Kiken S Batara. Saya adalah seorang programmer"
# print(nama)

nama_split = nama.split()
# print(nama_split)
nama_clear = nama.replace(".","").lower()
# print(nama_clear)

def clear_text (txt):
    gen = txt.replace(".","").replace(",",'').lower()
    # gen = txt.replace(",","").lower()
    return gen

coba1 = [clear_text(data) for data in nama.split()]
print (coba1)

