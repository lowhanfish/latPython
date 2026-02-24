

print("==================================")
mySet = {'a', 'b', 'c', 'd'}
mySet = set(('a', 'b', 'c', 'd'))
print(mySet)

print("==================================")

myList = ['a','a', 'b', 'c', 'd', 'd']
print(myList)
myList1 = myList.copy()
myList = set(myList)
print(myList)
myList1 = list(set(myList))
print(myList1)
print(myList1[0])
print("==================================")



