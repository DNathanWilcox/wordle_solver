fixed_letters = []
unfixed_letters = []
banned_letters = []

fixed_1 = '?'
fixed_2 = '?'
fixed_3 = '?'
fixed_4 = '?'
fixed_5 = '?'

fixed_word = fixed_word = [fixed_1, fixed_2, fixed_3, fixed_4, fixed_5]
unfixed_word = [[], [], [], [], []]

fixed_letter_range = int(input('Enter the amount of letters whose position you know: '))
unfixed_letter_range = int(input('Enter the amount of letters whose position you don\'t know: '))
banned_letter_range = int(input('Enter the amount of letters that are not in the word: '))

def build_fixed():
    if fixed_letter_range == 0:
        pass
    else:
        for i in range(fixed_letter_range):
            letter = input('Enter a letter with a known position: ')
            position = int(input(f'Enter the position of {letter}, 1-5: ')) - 1
            fixed_word[position] = letter
        return fixed_word

def build_unfixed():
    if unfixed_letter_range == 0:
        pass
    else:
        for i in range(unfixed_letter_range):
            index_count = 0
            letter = str(input('Enter a letter with an unknown position: '))
            position = int(input('Enter the position of the unknown letter: ')) - 1
            unfixed_letters.append(letter)
            unfixed_word[position].append(letter)
        return unfixed_letters

def build_banned():
    if banned_letter_range == 0:
        pass
    else:  
        for i in range(banned_letter_range):
            n = str(input('Enter a letter not in the word: '))
            banned_letters.append(n)
        return banned_letters

def add_fixed(new_fixed):
    for i in range(new_fixed):
        letter = input('Enter a letter with a known position: ')
        position = int(input(f'Enter the position of {letter}, 1-5: ')) - 1
        fixed_word[position] = letter
    return fixed_word

def add_unfixed(new_unfixed):
    for i in range(new_unfixed):
        index_count = 0
        letter = str(input('Enter a letter with an unknown position: '))
        position = int(input('Enter the position of the unknown letter: ')) - 1
        unfixed_letters.append(letter)
        unfixed_word[position].append(letter)
    print(unfixed_letters)
    return unfixed_letters

def add_banned(new_banned):
    for i in range(new_banned):
        n = str(input('Enter a letter not in the word: '))
        banned_letters.append(n)
    return(banned_letters)

def reconcile_fixed_unfixed():
    index_counter = 0
    for i in fixed_word:
        for j in unfixed_word:
            if i in unfixed_word[index_counter]:
                unfixed_word[index_counter].remove(i)

def check_unfixed(word):
    index_counter = 0
    for i in unfixed_letters:
        if i not in word:
            return False
    while index_counter <= 4:
        if word[index_counter] in unfixed_word[index_counter]:
            return False
        else:
            index_counter += 1
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

def crunch_words():
    possible_list = []
    for word in word_list:
        if (check_fixed(word) == True and check_banned(word) == True) and check_unfixed(word) == True:
            possible_list.append(word)
    print("Here are the possible words: \n\n")
    for i in possible_list:
        print(i)

def solve_wordle():
    wordle_solved = False
    build_fixed()
    build_unfixed()
    build_banned()
    while wordle_solved == False:
        crunch_words()
        check_solved = input("Did you solve it? Enter y/n: ")
        if check_solved == 'y':
            wordle_solved = True
        else:
            new_fixed = int(input('Enter the amount of new letters whose position you know: '))
            new_unfixed = int(input('Enter the amount of new letters whose position you don\'t know: '))
            new_banned = int(input('Enter the amount of new letters that are not in the word: '))
            add_fixed(new_fixed)
            add_unfixed(new_unfixed)
            add_banned(new_banned)
            reconcile_fixed_unfixed()

solve_wordle()