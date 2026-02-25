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