import sys
from stats import get_number_of_words, get_number_of_characters, get_sorted_number_of_characters


def get_book_text(book_path):
    with open(book_path, 'r', encoding="utf-8") as file:
        return file.read()
    

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}")

    #print(book_text[:1000])

    print("----------- Word Count ----------")
    get_number_of_words(book_text)

    print("------- Character Count ---------")
    number_of_characters = get_number_of_characters(book_text)
    sorted_number_of_characters = get_sorted_number_of_characters(number_of_characters)

    for character_key, count_value in sorted_number_of_characters.items():
        print(f"{character_key}: {count_value}")

    print("============= END ===============")

main()