user_input = input('take string:')

if not user_input:
    print('------')
for ch in user_input:
    if ch == "a":
        print (f'{user_input.index(ch)}')