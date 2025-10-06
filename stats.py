import string

def sort_on(items):
    return items["num"]

def get_num_words(book_content):
    content_arr = book_content.split()
    return len(content_arr)


def character_counter(book_content):
    # inisializing the dict {a: 0, b: 0 ....}
    counter = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    # creating a list of lower case letters
    lower_case_chars = list(string.ascii_lowercase)

    for element in book_content:
        element_lower = element.lower()
        if element_lower in lower_case_chars:
            counter[element_lower] += 1

    return counter


def sorted_character_count(char_count_dict):
    char_count_dicts = []

    for key, value in char_count_dict.items():
        char_count_dicts.append({"char": key, "num": value})

    char_count_dicts = sorted(char_count_dicts, key=sort_on, reverse=True)
    return char_count_dicts