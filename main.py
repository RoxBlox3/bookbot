from stats import char_counter, word_counter, sort


def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
    return file_contents


def main():
    count = word_counter(get_book_text("./books/frankenstein.txt"))
    char_list = char_counter(get_book_text("./books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    dict_list = sort(char_list)
    for entry in dict_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


main()
