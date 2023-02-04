number = 23
guess = int(input ('Напишить ціле число : '))

if guess == number:
    print(' ПОЗДОРОВЛЯЮ !! В тебе все вийшло ! ')
    print(' Але в мене немає для тебе ніякого подарунку, пробач. ')
elif guess < number:
    print(' Давай візьми трохи вишче ! ')
else :
    print(' Давай візьмемо трохи нижче ! ')
print(' Try again')

