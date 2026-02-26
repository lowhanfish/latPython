animals  = {
    'a' : "Ayam",
    'b' : "banteng",
    'c' : "Cacing",
    'd' : ["Kiken", "Rizwan", "Dayat"]
}

animals['h'] ="sumali"
print(animals)

print(type(animals))

# untuk mendapatkan keys dari dict
print(animals.keys())
print(animals.values())

a = animals['d']
a.insert(2, "Fajar")


print(animals.get('j',"Tidak di temukan"))

for data in a:
    print(data)



rumah = {
    "t36" : 150000,
    "t45" : 350000,
    "t72" : 450000,
    "t100" : [
        {
            "type" : 'Cash', 
            "price" : 950000, 
        },
        {
            "type" : 'Credit', 
            "price" : 1300000, 
        },
    ],
}


print(rumah)


bb = rumah["t100"]



for i, data in enumerate(bb):
    print(f"Untuk penjualan {data['type']} harganya adalah {data['price']}")