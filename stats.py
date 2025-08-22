def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    print(num_words, "words found in the document")
    return

def char_count(filepath):
    char_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        for letter in file_contents:
            if letter.lower() in char_dict:
                char_dict[letter.lower()] += 1
            else:
                char_dict[letter.lower()] = 1
    return char_dict