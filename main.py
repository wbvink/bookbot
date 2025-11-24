import sys
from stats import wordcount, char_count, sort_char_count

def get_book_text(input_path: str) -> str:
    """Read file (expects plaintext format) and return contents as string"""
    with open(input_path) as bookfile:
        book_contents = bookfile.read()
    return book_contents

def main():
    """Read book and print wordcount"""
    # Error handling: check whether a book path was given as second argument:
    if len(sys.argv) < 2:
        print("Error: No book path provided. Please provide the path to a plaintext book file as a command line argument.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    # Preparation:
    book_path = sys.argv[1] # this is where it used to be hardcoded to Frankenstein
    book_str = get_book_text(book_path)
    # wordcount:
    book_wordcount = wordcount(book_str)
    # character count:
    book_char_count = char_count(book_str)
    book_sorted_char_count = sort_char_count(book_char_count) # convert to list and sort
    book_sorted_filtered_char_count = []
    for di in book_sorted_char_count: # remove all non-letter characters from list
        if di["char"].isalpha():
            book_sorted_filtered_char_count.append(di)
    # create report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wordcount} total words")
    print("--------- Character Count -------")
    for di in book_sorted_filtered_char_count:
        print(f"{di["char"]}: {di["num"]}")
    
main()