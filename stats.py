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