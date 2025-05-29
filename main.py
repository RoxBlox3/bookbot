from stats import char_counter, word_counter, sort
import sys


def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        print(path)
        count = word_counter(get_book_text(path))
        char_list = char_counter(get_book_text(path))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        dict_list = sort(char_list)
        for entry in dict_list:
            print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")


main()
