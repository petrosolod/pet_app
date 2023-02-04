def printMax (a, b):
    if a > b :
        print ( a , 'biger that ', b)
    elif a == b :
        print ( a, 'Equal', b )
    else :
        print (b, 'biger that', a )

printMax(3, 5)  # прямая передача значений

x = 7
y = 12

printMax(x, y)  # передача переменных в качестве аргументов
