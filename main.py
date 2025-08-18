from stats import word_count
from stats import char_count

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents



def main():
    contents = get_book_text("/home/kayla/workspace/github.com/kaylap3/bookbot/books/frankenstein.txt")
    num_words = word_count(contents)
    num_char = char_count(contents)
    print(f"{num_words} words found in the document")
    print(num_char)

main()