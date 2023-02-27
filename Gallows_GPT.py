import random

# список слов для игры
words = ['яблоко', 'груша', 'апельсин', 'банан', 'клубника', 'ананас', 'вишня', 'слива']

# выбираем случайное слово
word = random.choice(words)

# создаем список из символов слова и заполняем его символами "_"
hidden_word = list("_" * len(word))

# количество попыток
attempts = 6

# список уже названных букв
used_letters = []

# функция для вывода информации об игре
def print_game_info():
    print("\nСлово:", " ".join(hidden_word))
    print("Ошибки:", attempts)
    print("Уже названные буквы:", ", ".join(used_letters))

# игровой цикл
while True:
    # выводим информацию об игре
    print_game_info()

    # запрашиваем у пользователя букву
    letter = input("Введите букву: ").lower()

    # проверяем, была ли уже введена эта буква
    if letter in used_letters:
        print("Вы уже называли эту букву!")
        continue

    # добавляем букву в список использованных
    used_letters.append(letter)

    # проверяем, есть ли эта буква в слове
    if letter in word:
        # если есть, заменяем соответствующий символ в скрытом слове
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
    else:
        # если нет, уменьшаем количество попыток
        attempts -= 1
        print("Нет такой буквы!")

    # проверяем, закончилась ли игра
    if attempts == 0:
        print("Вы проиграли! Слово было:", word)
        break
    elif "_" not in hidden_word:
        print("Вы выиграли! Слово было:", word)
        break
