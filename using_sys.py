import sys

print('Аргументи команндної строки : ')
for i in sys.argv : 
    print(i)

print('\n\nPYTHONPATH має в собі', sys.path)
#Доступ к переменной argv в модуле sys предоставляется при помощи точки,
#т.е. sys.argv. Это явно показывает, что это имя является частью модуля sys