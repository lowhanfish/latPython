
a = [2,3,4]

def hitung_total (a):
    # print(a)
    b = list(range(100))
    c = list((11,12,13,14))
    # print(c[1])
    return(b[0::5])

b= hitung_total(10)
b.append('hey')
b.pop()


while len(b):
    b.pop()
    # print(b)




def samples(a, b, c='minus'):
    if c == 'sum':
        return a+b
    elif c == 'minus':
        return a-b
    else:
        'not a number'




def performOperation(*args, **kwargs):
    print(args) # argumen
    print(kwargs) #keyword argument 
    print(type(args))
    print(type(kwargs))
# cc = performOperation(1,2,3,data ='uu', dataz='yuhu')


def defaultOperation(num1, num2, nama):
    print (locals())
    print(num1+num2)

cc = defaultOperation(1,2, nama="Rizwan")








