from stats import wordcount, char_count, sort_char_count

def get_book_text(book_path: str) -> str:
    """Read file (expects plaintext format) and return contents as string"""
    with open(book_path) as bookfile:
        book_contents = bookfile.read()
    return book_contents

def main():
    """Read Frankenstein and print wordcount"""
    frank_path = "books/frankenstein.txt"
    frank_str = get_book_text(frank_path)
    # wordcount:
    book_wordcount = wordcount(frank_str)
    # character count:
    book_char_count = char_count(frank_str)
    book_sorted_char_count = sort_char_count(book_char_count) # convert to list and sort
    book_sorted_filtered_char_count = []
    for di in book_sorted_char_count: # remove all non-letter characters from list
        if di["char"].isalpha():
            book_sorted_filtered_char_count.append(di)
    # create report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frank_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wordcount} total words")
    print("--------- Character Count -------")
    for di in book_sorted_filtered_char_count:
        print(f"{di["char"]}: {di["num"]}")
    
main()