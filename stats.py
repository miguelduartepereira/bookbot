def get_num_words(book):
    num_words = book.split()
    return len(num_words)

def get_num_characters(book):
    dict = {}
    for character in book:
        if character.lower() not in dict.keys():
            dict[character.lower()] = 1
            continue
        else:
            dict[character.lower()] += 1
    return dict

def get_list_dicts(dict):
    lst = []
    for key in dict:
        lst.append({"char": key, "num": dict[key]})
    lst.sort(reverse=True, key=sort_on)
    return lst
            
def sort_on(items):
    return items["num"]
