'''
На вход программе подается натуральное число nn, а затем nn целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел. 

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму данных чисел.
'''

counter = 0                         # here we will put all numbers
x = int(input())                    # x is how many iteration do we will have
for l in range(x):                  # l = variable for iteration(but we don't use it) (x = look above)
    counter = counter + int(input())# add number from couter to the counter + numbers from terminal 
print(counter) 
print(l)    