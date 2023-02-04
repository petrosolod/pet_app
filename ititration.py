s = input()

count_plus = 0
count_star = 0

for i in range(len(s)):
    if s[i] == "+":
        count_plus += 1
    if s[i] == "*":
        count_star += 1
print('Символ * встречается', count_star, 'раз')
print('Символ + встречается', count_plus, 'раз')

