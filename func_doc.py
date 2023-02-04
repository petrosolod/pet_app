def printMax(x,y):
    '''It seems like a comment, but its not a comment because you can call it 
    and you can make it as long as you like'''
    x = int(x)
    y = int(y)

    if x > y :
        print (x, 'is biger')
    else : 
        print(y, 'is biger')

printMax(3,5)
print(printMax.__doc__)
