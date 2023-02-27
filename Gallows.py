gallows = [['-', '-', '-', '-', '-', '-'],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ','|', ' ', ' ', ' ', ' '],
            [' ','|', ' ', ' ', ' ', ' '],
            [' ','|', ' ', ' ', ' ', ' '],
            ['/',' ', '\\', ' ', ' ', ' ']]

def draws_gallows(error_nums=0):
    
    def draw():
        str_gallows = ''
        for lst in gallows:
            str_gallows += ''.join(lst) + '\n'
        return str_gallows
    

    if not error_nums:
        return draw()
    if draws_gallows == 1:
        gallows[2][4] = 'o'
        return draw()
    if error_nums == 2:
        gallows[3][3] = '/'
        return draw()
    if error_nums == 3:
        gallows[3][4] = '|'
    if error_nums == 4:
        gallows[3][5] = '/'
    if error_nums == 6:
        gallows[4][5] = '\\'



for lst in gallows:
    print (''.join(lst))

word = "pizza"

answer_wodr = ["_" for _ in range(len(word))]

print (" ". join(answer_wodr))
#user_input = input("Type your letter>>>")


def find_all(text:str, substring):
    result = []
    start_position = 0
    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position > -1:
            result.append(position)
            start_position = position + 1
    return result

errors_count = 0
while "".join(answer_wodr) != word:
    user_input = input("Type your letter>>>")
    
    if user_input in word:
        letter_indexes = find_all(word, user_input)
        for i in letter_indexes:
            answer_wodr[i] = user_input
        print(draws_gallows())
        print(" ". join(answer_wodr))
    else:
        errors_count += 1
        print(" ". join(answer_wodr))
    

    if errors_count >= 6:
        print ("Game over")
        break

print ("You winn")

