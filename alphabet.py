alphabet = ' abcdefghijklmnopqrstuvwxyz'
alpha_list = []

for i in range(len(alphabet)):
    alpha_list.append(alphabet[i] * i)
    #print(alphabet[i])
del alpha_list[0]
print(alpha_list)

