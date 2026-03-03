

def triangle(num):
    if num == 1:
        return num
    else:
        value = 0
        for data in range(num, 0, -1):
            value += data
        return value


def triangle2(num):
    if num == 1:
        return num
    else:
        value = num*(num+1)/2
        return value
    
    #n(n+1)/2
    #t(n)+t(n-1)

def triangle3(num):
    if num == 1:
        return num
    return num + triangle3(num-1)


def trianglex(num):
    if num == 1:
        return num
    return num + trianglex(num - 1)

def square(num):

   valuex = trianglex(num)+trianglex(num-1)
   return valuex

dddd = square(5)





result = triangle(5)
result2 = triangle2(5)
result3 = triangle3(5)
# print(result)
# print(result2)
print(dddd)


def someFunc(func):
    print(func(5) + 2)

print(someFunc(lambda x: x * 3))