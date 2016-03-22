#Pig Latin translator

##consider adding an if statement for line break if len(pig_latin_word_list) > int(x)

def prompt_user_for_sentence():
    """prompt the user to enter a sentence as a string.  return the sentence."""
    return input('Please type a sentence you wish to translate: \n')

def convert_english_sentence_into_word_list(english_sentence):
    """break the user sentence into individual words to be translated. return the list of words"""
    new_list = english_sentence.split()
    return new_list

def return_endword_punctuation(word):
    """tests the final char of a word for punctuation.  returns the punctuation or 
    an empty string if no punctuation as a value."""
    punctuation_list = ['!', '?', '.', ';', ':', '\'', '"', '_', '-']
    if word[-1] in punctuation_list:
        punctuation_char = word[-1]
    else:
        punctuation_char = ""
    return punctuation_char
#see note in translate_word_to_pig_latin regarding 'my'
def translate_word_to_pig_latin(english_word):
    """takes a english_word, tests it against the rules of pig latin, and translates.  
    returns the pig latin.   problem with word 'my'"""
    vowels_list = ['a', 'e', 'i', 'o', 'u']

    first_letter = english_word[0]
    default_pig_ending = 'ay'
    vowel_word_pig_ending = 'yay'

    if len(english_word) == 1:
        second_letter = ""
        remainder_letters = ""
    else:
        second_letter = english_word[1]
        remainder_letters = english_word[2:]
    #Need to figure out how to deal with 2 character strings where 'y' is second letter, as with 'my'
    if first_letter not in vowels_list and second_letter not in vowels_list:
        pig_latin_word = remainder_letters + first_letter + second_letter + default_pig_ending

    elif first_letter in vowels_list:
        pig_latin_word = first_letter + second_letter + remainder_letters + vowel_word_pig_ending

    else:
        pig_latin_word = second_letter + remainder_letters + first_letter + default_pig_ending

    return pig_latin_word
 
def create_pig_latin_word_list(english_sentence_word_list):
    """takes in the list of english words, translates each word using pig latin rules, and
    adds it to the pig latin list of words.  returns the pig latin list of words."""
    pig_latin_word_list = []

    for word in english_sentence_word_list:

        word_final_punctuation = return_endword_punctuation(word)

        if word_final_punctuation != "":
            word = word[0:-1]

        pig_latin_word = translate_word_to_pig_latin(word) + word_final_punctuation

        pig_latin_word_list.append(pig_latin_word)

    return pig_latin_word_list

def combine_words_into_sentence(pig_latin_sentence_word_list):
    """combines each word from a list into a sentence string.  returns the sentence."""
    pig_sentence = ' '.join(pig_latin_sentence_word_list)
    return pig_sentence


english_sentence = prompt_user_for_sentence()

english_sentence_word_list = convert_english_sentence_into_word_list(english_sentence)

pig_latin_word_list = create_pig_latin_word_list(english_sentence_word_list)

pig_latin_sentence = combine_words_into_sentence(pig_latin_word_list)

print('translates into: ', pig_latin_sentence)
