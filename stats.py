def stats(book_path):
    text = get_book_text(book_path)
    # print(text)
    words = text.split()
    char_count_dict = char_dict(text)
    char_list = sort_char_dict(char_count_dict)
    print(f"Analysis of {book_path}")
    print()
    print(f"Found {len(words)} total words")
    print()
    print("characters and their count:")
    for char in char_list:
        print(f"{char["char"]}: {char["num"]}")
        
def sort_on(dict):
    return dict["num"]

def sort_char_dict(dict):
    list = []
    for d in dict:
        if d.isalpha():
            list.append({"char": d, "num": dict[d]})
    list.sort(reverse=True, key=sort_on)
    return list

def char_dict(text):
    chars = {}
    for char in text:
        lowercase = char.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()