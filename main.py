from stats import wordcount

def get_book_text(book_path: str) -> str:
    """Read file (expects plaintext format) and return contents as string"""
    with open(book_path) as bookfile:
        book_contents = bookfile.read()
    return book_contents

def main():
    """Read Frankenstein and print wordcount"""
    frank_str = get_book_text("books/frankenstein.txt")
    book_wordcount = wordcount(frank_str)

    print(f"Found {book_wordcount} total words")

main()