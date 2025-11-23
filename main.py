def get_book_text(book_path) -> str:
    """Read file (expects plaintext format) and return contents as string"""
    with open(book_path) as bookfile:
        book_contents = bookfile.read()
    return book_contents

def main():
    """Read Frankenstein and print it to the console"""
    frank_str = get_book_text("books/frankenstein.txt")
    print(frank_str)

main()