def total ( initial = 5, *numbers, extra_number = 1): 
    count = initial 
    for number in numbers :
        count = count + number  #теж саме що \count += number\
    count += extra_number
    print(count)

total(10,1,2,3,extra_number=50)
total(10,1,2,3)
#одна зірочка = КОРТЕЖ(tuple) -- дві зірочки - СЛОВНИК(dict)