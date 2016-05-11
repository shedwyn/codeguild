def dwnld_book_into_text_lines_list():  # could be made input so to limit the
    # number scanned
    with open('A_Modest_Proposal_stripped.txt') as raw_book_file:
        # Pygmalion_stripped.txt or A_Modest_Proposal_stripped.txt
        book_as_line_strings = raw_book_file.readlines()
    return book_as_line_strings


def strip_specific_char_from_word(text_word):
    """takes in the text_word and strips end and fore punctuation.  returns
    word_without_punc."""
    word_without_punc = text_word.strip('.!,:;?_-()')
    return word_without_punc


def remove_word_punctuation_loop(book_as_words):
    """takes in the list of words, strips punctuation from front and end.
    returns new list"""
    book_as_words_without_end_punct = []
    for word_with_punct in book_as_words:
        word_without_punct = strip_specific_char_from_word(word_with_punct)
        book_as_words_without_end_punct.append(word_without_punct)

    return book_as_words_without_end_punct


def clean_unneccesary_non_alpha_char(book_as_words):
    """takes in list of single words, strips elements that are stand alone
    carriage returns.  returns book_as_words_without_non_alpha_char"""

    book_as_words_without_end_punct = remove_word_punctuation_loop(
        book_as_words
    )

    count_of_returns = book_as_words_without_end_punct.count('\n')

    while count_of_returns > 0:

        book_as_words_without_end_punct.remove('\n')
        count_of_returns -= 1

    book_as_words_without_non_alpha_char = book_as_words_without_end_punct

    return book_as_words_without_non_alpha_char


def break_book_into_cleaned_words():
    """takes in nothing.  generates list of text words as string.
    returns list."""
    book_as_line_strings = dwnld_book_into_text_lines_list()
    text_as_single_string = ' '.join(book_as_line_strings).upper()
    book_as_words = text_as_single_string.split()  # for word in text_words_raw
    book_as_words_without_punctuation = clean_unneccesary_non_alpha_char(
        book_as_words
    )
    book_as_cleaned_words = book_as_words_without_punctuation

    return book_as_cleaned_words


def create_counting_dictionary():
    """takes in list of word strings, returns dictionary of word/pairs and
    their corresponding frequency in the book.  This function was first
    developed with single words in mind, hence references in the singular
    case."""
    word_to_counts = {}
    stripped_book_words = break_book_into_cleaned_words()
    for word in stripped_book_words:
        if word not in word_to_counts:
            word_to_counts[word] = 1
        elif word in word_to_counts:
            word_to_counts[word] += 1
            # name, number = line_string.split()
    return word_to_counts


def find_count_for_word_in_book(word_to_find, word_to_counts):
    if word_to_find not in word_to_counts:
        return 0
    else:
        return word_to_counts[word_to_find]


def main(word):
    word_to_find = word
    word_to_counts = create_counting_dictionary()
    count_for_word_to_find = find_count_for_word_in_book(
        word_to_find, word_to_counts
    )

if __name__ == '__main__':
    main()
