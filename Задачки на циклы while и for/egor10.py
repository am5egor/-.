game = ['war tander', 'airpiane', 'standoff 2', 'fish world', 'world of tanks']
searching = input('введите свой запрос:').lower()
if searching in game:
    print('запрос найден')
else:
    print('запрос не найден')
