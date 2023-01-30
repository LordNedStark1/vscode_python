value = "i hate precious with all [] my heart and soul [] and body and[]  everything because she []is of type Chibuzor"
v = value.split("[]", 5)

lis_v, word_dict = [], {}

count = len(v) - 1

for i in range(len(v)):
    lis_v.append(v[i:len(v) - count])
    word_dict[i * 2] = v[i:len(v) - count]
    count = count - 1

vav = []

[vav.append(lis_v[i][0].strip().split(" ")) for i in range(len(lis_v))]

coun = 0
row= 0
colm = 0

for e in range (len(vav)):
    for r in range (e):
        



# for e in range(len(vav)):
#     # print(vav[e])
#     for r in range(e):
#         # print(r)
#         if vav[e] == vav[e][r]:
#             coun = coun + 1
            
#         print(coun)
