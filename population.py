''' 
На вход программе подается три натуральных числа m,p,n:

    m: стартовое количество организмов;
    p: среднесуточное увеличение в %;
    n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов. 
Программа должна выводить размер популяции в каждый день, начиная с 11 и заканчивая n-м днем.

Формат входных данных :
На вход программе подается три натуральных числа.'''

m, p, n = int(input()), int(input()), int(input())
x = m * p/100
for l in range(0, n) :
    print(l+1, m * (p / 100 + 1) ** l)
#kjdnfkjkjdf