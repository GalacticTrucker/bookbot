def get_number_of_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_number_of_characters(text):
    characters = {}
    for char in text.lower():
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def get_sorted_number_of_characters(characters):
    #characters.sort( key=characters.get(), reverse=True)
    sorted_characters = dict(sorted(characters.items(), key=sort_by_value, reverse=True))
    return sorted_characters

def sort_by_value(item):
    return item[1]