#Pig Latin translator


def prompt_user_sentence():
    """prompt the user to enter a sentence.  return the sentence."""
    return input('Please type a sentence you wish to translate: \n')

def convert_sentence_into_word_list(sentence_string):
    new_list = sentence_string.split()
    """break the user sentence into individual words to be translated. return the list of words"""
    return new_list

def remove_endword_punctuation(word):
    """tests the final char of a word for punctuation.  returns that value."""
    punctuation_list = ['!', '?', '.', ';', ':', '\'', '"', '_', '-']
    if word[-1] in punctuation_list:
        punctuation_char = word[-1]
    else:
        punctuation_char = ""
    return punctuation_char

def translate_word_to_pig_latin(word):
    """takes a word, tests it against the rules of pig latin, and translates.  returns the pig latin word"""
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    first_letter = word[0]
    default_pig_ending = 'ay'
    vowel_word_pig_ending = 'yay'

    if len(word) == 1:
        second_letter = ""
        remainder_letters = ""
    else:
        second_letter = word[1]
        remainder_letters = word[2:]

    if first_letter not in vowels_list and second_letter not in vowels_list:
        pig_latin_word = remainder_letters + first_letter + second_letter + default_pig_ending

    elif first_letter in vowels_list:
        pig_latin_word = first_letter + second_letter + remainder_letters + vowel_word_pig_ending

    else:
        pig_latin_word = second_letter + remainder_letters + first_letter + default_pig_ending

    return pig_latin_word
 
def create_pig_latin_word_list(word_list):
    
    list_of_pig_latin_words = []

    for word in word_list:

        word_final_punctuation = remove_endword_punctuation(word)

        if word_final_punctuation != "":
            word = word[0:-1]

        pig_latin_word = translate_word_to_pig_latin(word) + word_final_punctuation

        list_of_pig_latin_words.append(pig_latin_word)

    return list_of_pig_latin_words

def combine_words_into_sentence(word_list):
    """combines each word from a list into a sentence string.  returns the sentence."""
    pig_sentence = ' '.join(word_list)
    return pig_sentence


english_sentence = prompt_user_sentence()

list_of_english_sentence_words = convert_sentence_into_word_list(english_sentence)

pig_latin_sentence = combine_words_into_sentence(create_pig_latin_word_list(list_of_english_sentence_words))

print('translates into: ', pig_latin_sentence)
