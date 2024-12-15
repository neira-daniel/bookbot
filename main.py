def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as file:
        text = file.read()
    word_counter = get_number_of_words(text)
    character_frequency = get_character_frequency(text)
    characters_ordered_by_frequency = sort_dictionary_on_value(character_frequency)
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_counter} words found in the document")
    for character in characters_ordered_by_frequency:
        if character[0].isalpha():
            print(f"The {repr(character[0])} character was found {character[1]} times")
    print("--- End report ---")


def get_number_of_words(text: str):
    return len(text.split())


def get_character_frequency(text: str):
    lowercase_text = text.lower()
    available_characters = list(set(lowercase_text))
    character_frequency = {letter: 0 for letter in available_characters}
    for character in lowercase_text:
        character_frequency[character] += 1
    return character_frequency

def sort_dictionary_on_value(d: dict):
    new_d = [(key, d[key]) for key in d.keys()]
    return sorted(new_d, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    main()
