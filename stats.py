def get_num_words(text):
    return len(text.split())


def get_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_dict(dict):
    list_of_dicts = []
    for key in dict:
        list_of_dicts.append({"char": key, "num": dict[key]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
