def total(a=5, *numbers, **phonebook): #одна зірочка = КОРТЕЖ(tuple) -- дві зірочки - СЛОВНИК(dict)
    print('a', a)

    #проход по всем элементам кортежа
    for single_item in numbers :
        print('single_items', single_item)

    #проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total( 1, 2, 3,12, 15, Jack=1123, Jhon=2231, Inge=1560))
