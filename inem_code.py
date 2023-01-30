introductions = "My name is Inemesit Inyang Udousoro, i am 18 years years years years old and i hail from Akwa Ibom State."
split_intro = introductions.split(" ")
print(split_intro)

intro_1 = introductions[:10]
intro_2 = introductions[11:36]
intro_3 = introductions[37:45]
intro_4 = introductions[45:58]
intro_5 = introductions[59:70]
intro_6 = introductions[71:87]

grouped_words = []

grouped_words.append(intro_1)
grouped_words.append(intro_2)
grouped_words.append(intro_3)
grouped_words.append(intro_4)
grouped_words.append(intro_5)
grouped_words.append(intro_6)

# print(grouped_words)

count = 0;
count_two=0
count_similar_words = []

 
# for i in range(len(split_intro)):
#     split_intro[i]
#     for j in range(len(split_intro)):
#         if split_intro[i] == split_intro[j]:
#            count += 1
#            if count >1:
#             count_two +=1            
#             print(count_two)
#             count =0
#             print (split_intro[j])

# count_similar_words = []


for i in range (len(split_intro)):
    count_similar = split_intro.count(split_intro[i])
    if count_similar> 1:
      print (split_intro[i])
      print(count_similar)