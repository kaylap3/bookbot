def word_count(text):
    words = text.split()
    return len(words)

def char_count(book_text):
    num_char = {}
    text = book_text.lower()
    for char in text:
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char

def sort_on(char_dict):
    return char_dict["num"]

def create_to_list(char_counts):
    new_list = []
    for char in char_counts:
        count = char_counts[char]
        new_dict ={"char": char, "num": count}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list