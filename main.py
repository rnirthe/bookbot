import sys
from stats import get_num_words, get_chars, sort_dict


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]


def main():
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    num_chars = get_chars(book_text)
    fancy = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in fancy:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


main()
