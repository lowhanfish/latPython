textt = "Sebagai ASN..! di tuntut untuk memiliki integritas yang kuat. ASN yang baik mengutamakan integritas dan intelektual"
# normalisasi
clear1 = (
    textt.lower()
        .replace(".", "")
        .replace(",", "")
        .replace("!", "")
        .split()
)
# comprehension1 = {data : 0 for data in clear1}
# print(comprehension1)

valx = {}

for data in clear1:
    if data in valx:
        valx[data] += 1
    else:
        valx[data]= 1

# print(valx)



def encodeString (kata):
    if len(kata):
        huruf = kata[0]
        count_huruf = 1
        result = []
        for data in kata[1:]:
            if huruf ==  data:
                count_huruf +=1
            else:
                result.append((huruf, count_huruf))
                huruf =  data
                count_huruf = 1
        result.append((huruf, count_huruf))
        return result
    else:
        return []

kata = "AAAAIIUUUEOOOOAII"

def decodeString(arr):
    text_arr = []
    for huruf,jumlah in arr:
        text_arr.append(huruf*jumlah)
    return "".join(text_arr)

arrx = [('A', 4), ('I', 2), ('U', 3), ('E', 1), ('O', 4), ('A', 1), ('I', 2)]

# result1 = encodeString(kata)
# result2 = decodeString(arrx)
# print (result1)
# print (result2)


# ============== EVALUATION ==============

words = "AAAAIIIUAAEEOOIIIUUUUU"

#[("A":4),("I":3),("U":1),("A":2)...]



if not words:
    print([])
else:
    char = words[0]
    count = 1
    list_data = []
    for data in words[1:]:
        if char == data:
            count += 1
        else:
            list_data.append((char, count))
            count = 1
            char = data

    list_data.append((char, count))

    print(list_data)


print("=======================")
data_list = [('A', 4), ('I', 3), ('U', 1), ('A', 2), ('E', 2), ('O', 2), ('I', 3), ('U', 5)]

if len(data_list) <1:
    print("Array Kosong gez!")
else:
    text = ""
    listx = []
    for data in data_list:
        for countx in range(data[1]):
            listx.append(data[0])
    text = "".join(listx)
    print(text)


# [{"A": 6}, {"I": 6}]


for data in data_list:
    pass


