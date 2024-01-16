from random import randint

generate = randint(1, 10)
numb = int(input('введите любое число от 1 до 10:'))
counter = 1

while numb != generate:
    print('сожелеем вы не угадали')
    counter += 1
    numb = int(input('введите любое число от 1 до 10'))
print('поздравляем, вы угадали')
print('число попыток:', counter)