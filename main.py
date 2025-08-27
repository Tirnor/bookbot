from stats import get_book_text
from stats import char_count
import sys


def main ():
    if len(sys.argv) == 2:
        get_book_text(sys.argv[1])
        char_count(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return
main()