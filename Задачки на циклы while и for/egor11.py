games =[]
game = input('введите название игры:').lower()
while game != '0':
    if game in games:
        print('эта игра уже введена')
    else:
        games.append(game)
    game = input('введите название игры:').lower()
games.sort()   
print('список игр', games)
