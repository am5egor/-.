niknames = ['gup', 'polkar', 'tampa', 'amber']
niknames.sort()
amount = len(niknames)
i = 1
print('список пользователей')
for nikname in niknames:
    print(i, '-', nikname)
    i += 1
print('всего пользователей:', amount)
