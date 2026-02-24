print("==========================================")
print("======== List Play Ground ======")
myList = [1,2,3,4,5]
print(myList[2:5])
print(myList[2:])
print(myList[:5])

print(myList[0:6:2])
print(myList[::3])
print(myList[::-2])

print("==========================================")
print("======== LIST WITH RANGE ======")

# for i in range(100):
#     print(i)

myList = list(range(100))

print(myList)
print("--------------------")
print(myList[::5])
print("--------------------")

print("==========================================")
print("======== MODIFYING LIST ======")

myList = [1,2,3,4,5]
myList.append(20)
print(myList)
print("--------------------")
# Untuk menambah data pada array di list tertentu
myList.insert(2, "New Value in index 2")
print(myList)
print("--------------------")
# Untuk menghapus data pada array berdasarkan valuenya
myList.remove("New Value in index 2")
print(myList)
print("--------------------")
# Untuk menghapus data pada array untuk index terahir
myList.pop()
print(myList)

print("--------------------")
while len(myList):
    print(myList.pop())

print(myList)
print("--------------------")

a = [1,2,3,4,5]
b = a
c = a.copy()

a.append(6)
print(a)
print(b)
print(c)

print("--------------------")