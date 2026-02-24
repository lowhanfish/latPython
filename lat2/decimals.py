from decimal import Decimal, getcontext

getcontext().prec=2
# print (int('100', 2))
# print(getcontext())

a = Decimal(1)/Decimal(3)
b = round(1.2/2.5, 1)

print(b)