import sys
from stats import *

def main():
    if len(sys.argv) == 2:
        Filepath = sys.argv[1]
    else:
        Filepath = "books/frankenstein.txt"

    try:
        file_contents = get_book_text(Filepath)
    except FileNotFoundError:
        print(f"Error: Could not find the book at {Filepath}")
        sys.exit(1)

    num_words = words_in_book(file_contents)
    letters = letter_count(file_contents)
    
    sorted_list = chars_dict_to_sorted_list(letters)
    text_word_total = f"Found {num_words} total words"
    
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {Filepath}...
    ----------- Word Count ----------
    {text_word_total}
    """)
    
    # This matches the assignment requirement to print the sorted tuple list directly
    for item in sorted_list:
        print(item)
        
    print("""============= END ===============""")


main()