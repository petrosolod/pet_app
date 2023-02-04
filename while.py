number = 23
running = True

while running: # Все що йде далі, трапляєтся в блоці while
    guess = int(input(' Введіть ціле значення : '))

    if guess == number:
        print(' Все супер, ти вгадав.')
        running = False  #це зупинить цикл while
    elif guess < number:
        print(' Це погана ідея, бери вижче ! ')
    else:
        print(' А тут треба нижче взяти')
else: # Ось тут блок While закінчився
    print(' Цикл while зупинено')
print(' Finish')
