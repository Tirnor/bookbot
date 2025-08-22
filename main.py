from stats import get_book_text
from stats import char_count


def main ():
    booktext = get_book_text("books/frankenstein.txt")
    print(char_count("books/frankenstein.txt"))
    return booktext

main()