from stats import get_num_words, count_characters, sort_character_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = get_num_words(book_text)
        character_count = count_characters(book_text)
        sorted_characters = sort_character_count(character_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for x in sorted_characters:
            if x[0].isalpha():
                print(f"{x[0]}: {x[1]}")
        return

main()
