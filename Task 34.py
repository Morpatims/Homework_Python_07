count_vowels = lambda word: sum(1 for letter in word if letter in 'аеёиоуыэюя')

rhythm = lambda s: len(set(map(count_vowels, s.split()))) == 1

str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print('Парам пам-пам' if rhythm(str_1) else 'Пам парам')