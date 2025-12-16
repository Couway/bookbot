def num_of_words(content):
    words = content.split()
    return len(words)

def num_of_symbols(content):
    symbols = {}
    for s in content.lower():
        symbols[s] = symbols.get(s, 0) + 1
    
    return symbols

def sort_on(dict):
    return dict["num"]

def get_report(characters):
    char_list = []
    char_dict = {}
    for char in characters:
        if char.isalpha():
            entry = {"char": char, "num": characters[char]}
            char_list.append(entry)
        
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list


    