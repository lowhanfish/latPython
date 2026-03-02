animals = {
    "a" : ["Lion", "Tiger", "Puma", "Cat"],
    "b" : ["Eagle"],
    "c" : ["Chicken"],
    "d" : ["Wolf", "Dog", "Hiena"]
}

for key, values in animals.items():
    if len(values) > 1:
        # print(f"animals : {values}")
        continue
    print(f"animals only one : {values}")


for number in range(2,100):
    for factor in range(2, int(number**0.5)+1):
        if number % factor == 0:
            break
    else:
        print(f"Number {number} is prime!")