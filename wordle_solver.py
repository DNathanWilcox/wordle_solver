fixed_letters = []
fixed_letters_position = []
unfixed_letters = []
banned_letters = []

fixed_1 = '?'
fixed_2 = '?'
fixed_3 = '?'
fixed_4 = '?'
fixed_5 = '?'

fixed_word = [fixed_1, fixed_2, fixed_3, fixed_4, fixed_5]

fixed_letter_range = int(input('Enter the amount of letters whose position you know: '))
unfixed_letter_range = int(input('Enter the amount of letters whose position you don\'t know: '))
banned_letter_range = int(input('Enter the amount of letters that are not in the word: '))

def build_fixed():
    for i in range(fixed_letter_range):
        letter = input('Enter a letter with a known position: ')
        position = int(input(f'Enter the position of {letter}, 1-5: ')) - 1
        fixed_word[position] = letter
    return fixed_word

def build_unfixed():
    for i in range(unfixed_letter_range):
        n = str(input('Enter a letter with an unknown position: '))
        unfixed_letters.append(n)
    return unfixed_letters

def build_banned():
    for i in range(banned_letter_range):
        n = str(input('Enter a letter not in the word: '))
        banned_letters.append(n)
    return(banned_letters)

def check_unfixed(word):
    for i in unfixed_letters:
        if i in word:
            continue
        else:
            return False
            break
    return True

def check_fixed(word):
    count = 0
    for i in fixed_word:
        if i != '?':
            if i == word[count]:
                count += 1
                continue
            else:
                return False
                break
        else:
            count += 1
            continue
    return True

def check_banned(word):
    for i in banned_letters:
        if i in word:
            return False
            break
        else:
            continue
    return True

word_list = []
with open('five_character_words.csv', 'r') as file:
    for i in file:
        word_list.append(i)

def solve_wordle():
    possible_list = []
    if unfixed_letter_range == 0:
        build_fixed()
        build_banned()
        for word in word_list:
            if check_fixed(word) == True and check_banned(word) == True:
                possible_list.append(word)
        for i in possible_list:
            print(i)
    
    elif fixed_letter_range == 0:
        build_unfixed()
        build_banned()
        for word in word_list:
            if check_unfixed(word) == True and check_banned(word) == True:
                possible_list.append(word)
        for i in possible_list:
            print(i)
    else:
        build_fixed()
        build_unfixed()
        build_banned()
        for word in word_list:
            if check_fixed(word) == True and check_unfixed(word) == True and check_banned(word) == True:
                possible_list.append(word)
        for i in possible_list:
            print(i)

solve_wordle()