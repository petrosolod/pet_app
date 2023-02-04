def maximum(x, y):
    if x > y:
        return (x, ' is BIGER')
    elif y == x:
        return (y, 'Equal')
    else:
        return (y, ' is BIGER')


print(maximum(5, 3))
