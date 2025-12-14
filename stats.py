def get_num_words(fulltext):
    num_word = fulltext.split()
    return len(num_word)

def get_num_char(fulltext):
    char_list = fulltext.lower()
    char_dict = {}
    for chars in char_list:
        if chars in char_dict:
            char_dict[chars] += 1
        else:
            char_dict[chars] = 1
    return char_dict

def sort_on(item):
    return item["num"]

def sort_chars(fulltext):
    chars_dict = get_num_char(fulltext)
    sort_list = []
    for char in chars_dict:
        sort_list.append({"char": char, "num": chars_dict[char]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
