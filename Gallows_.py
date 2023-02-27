from random import choice

gallows = [["-", "-", "-", "-", "-", "-",],
        [" ", "|", " ", " ", "| ", " ",],
        [" ", "|", " ", " ", " ", " ",],
        [" ", "|", " ", " ", " ", " ",],
        [" ", "|", " ", " ", " ", " ",],
        ["/", " ", "\\", " ", " ", " ",]]
def draws_gallows(error_nums = 0):
    def draw():
        str_gallows = ""
        for lst in gallows:
            str_gallows += "".join(lst) + "\n"
        return str_gallows
    if error_nums == 1:
        gallows[2][4] = "O"
    if error_nums == 2:
        gallows[3][3] = "/"
    if error_nums == 3:
        gallows[3][4] = "|"
    if error_nums == 4:
        gallows [3][5] = "\\"
    if error_nums == 5:
        gallows[4][3] = "/"
    if error_nums == 6:
        gallows[4][5] = "\\"
    return draw()

def find_all(text:str, substring):
    result = []
    start_position = 0
    for i in range(len(text)):
        position = text.find(substring, start_position)
        if position > -1:
            result.append(position)
            start_position = position + 1
    return result

def main():
    word = choice(["pizza"], ["fdfsd"], ["qweqweqw"], ["weqweqw"])
    answer_word = ["_" for _ in range(len(word))]
    print(draws_gallows())
    print(" ".join(answer_word))
    error_count = 0
    lose = False
    
    while "".join(answer_word) != word:
        user_input = input("Type your letter >>> ").lower()
        
        if user_input in word:
            letter_index = find_all(word, user_input)
            for i in letter_index:
                answer_word[i] = user_input
            print(draws_gallows(error_count))
            print(" ".join(answer_word))
        else:
            error_count += 1
            print(draws_gallows(error_count))
            print(" ".join(answer_word))
        if error_count >= 6:
            lose = True
            break
    if lose == True:
        print("Game over \n You Lose !")
    else:
        print("You won !")

if __name__ == "__main__":
    main()