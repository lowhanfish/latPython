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

result1 = encodeString(kata)
result2 = decodeString(arrx)
print (result1)
print (result2)


