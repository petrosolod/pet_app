def func_outer():
    x = 5
    print('x equal', x)

    def func_inner():
        nonlocal x
        x = 10

    func_inner()
    print('Local x change to', x)


func_outer()
