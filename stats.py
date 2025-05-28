def word_counter(book):
    counter = 0
    words = book.split()
    for word in words:
        counter += 1
    return counter


def char_counter(book):
    chars = {}
    book = book.lower()
    for letter in book:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def sort(dictionary):
    dictionary_list = []
    for entry in dictionary:
        diction = {"char": entry, "num": dictionary[entry]}
        dictionary_list.append(diction)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
