import sys
from stats import word_count
from stats import char_count
from stats import create_to_list

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents



def main():
    contents = get_book_text(sys.argv[1])
    num_words = word_count(contents)
    num_char = char_count(contents)
    sort_char_count = create_to_list(num_char)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sort_char_count:
        char = item["char"]
        count = item["num"]
        if char.isalpha() == True:
             print(f"{char}: {count}")
        

main()