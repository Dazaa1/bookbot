from stats import get_num_words, character_counter, sorted_character_count
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        book_content = f.read()

    return book_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    book_content = get_book_text(book_name)
    book_words_count = get_num_words(book_content)
    char_count_dict = character_counter(book_content)
    char_count_dicts = sorted_character_count(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print("--------- Character Count -------")
    for element in char_count_dicts:
        print(f"{element['char']}: {element['num']}")

    print("============= END ===============")

main()