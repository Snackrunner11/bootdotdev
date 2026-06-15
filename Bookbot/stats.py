def get_book_text(Filepath):
    with open(Filepath) as f:
        file_contents = f.read()
    return file_contents

def words_in_book(file_contents):
    text = file_contents
    word_count_list = text.split()
    words_number = len(word_count_list)
    return words_number

def letter_count(text):
    letters = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0,
        "g":0, "h":0, "i":0, "j":0, "k":0, "l":0,
        "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
        "s":0, "t":0, "u":0, "v":0, "w":0, "x":0,
        "y":0, "z":0}
    lowercase_text = text.lower()
    for letter in lowercase_text:
        if letter in letters:
            letters[letter] = letters[letter] + 1
    return letters

def sort_on(character_tuple):
    return character_tuple[1]

def chars_dict_to_sorted_list(letters):
    list_with_tuples = []
    
    for letter, value in letters.items():
        list_with_tuples.append((letter, value))
        
    sorted_list = sorted(list_with_tuples, reverse=True, key=sort_on)
    
    return sorted_list