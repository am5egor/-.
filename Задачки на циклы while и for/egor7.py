password = input('введите имя:')
wrong = '@ = ? - # $'
for symbol in password:
    if symbol in wrong:
        print('внимание запрещённый символ', symbol)