def get_text_contents(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    return content

def count_words(content):
    words = content.split()
    
    return len(words)

def count_all_characters_as_dict(content):
    character_counts = {}
    for characters in content:
        character_cased = characters.lower()
        if character_cased in character_counts:
            character_counts[character_cased] = character_counts[character_cased] + 1
        else:
            character_counts[character_cased] = 1

    return character_counts

def filter_characters_by_letters(character_counts):
    filtered_characters = {}
    for character in character_counts:
        if character.isalpha():
            filtered_characters[character] = character_counts[character]
    
    return filtered_characters

def create_character_count_string(character_counts):
    full_character_count_string = ""
    sorted_character_counts = sort_dict_by_value(character_counts, True)
    for character in sorted_character_counts:
        full_character_count_string = full_character_count_string + f"The {character} character was found {sorted_character_counts[character]} times\n"

    return full_character_count_string

def sort_dict_by_value(dictionary, descending):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=descending))

def get_formatted_book_report(file_path):
    #handle intro/outro strings
    book_report_intro = f"--- Begin report of {file_path} ---"
    book_report_outro = f"--- End report ---"

    book_report = book_report_intro + "\n"

    #handle word count
    word_count = count_words(get_text_contents(file_path))
    book_report = book_report + f"{word_count} words found in the document\n"
    
    #handle arbitrary spacing
    book_report = book_report + "\n\n"

    #handle character counts
    book_report = book_report + create_character_count_string(filter_characters_by_letters(count_all_characters_as_dict(get_text_contents(file_path))))

    #handle outro string
    book_report = book_report + book_report_outro

    return book_report

print (get_formatted_book_report("books/frankenstein.txt"))


