def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def count_characters(text):
    characters = {}
    for c in text:
        if c.lower() in characters:
            characters[c.lower()] += 1
        else:
            characters[c.lower()] = 1
    return characters

def sort_character_count(character_count):
    character_dict = character_count.items()
    sorted_characters = sorted(character_dict, key=lambda x: x[1], reverse=True)
    return sorted_characters
