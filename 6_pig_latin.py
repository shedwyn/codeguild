#Pig Latin translator
#enter sentence
#translate to pig latin
#print out

#bonus/advanced - handle vowels with punctuation, punctuation, handle capitalization

#take first letter
#move to end
#add 'ay' on new end

#'cat' - 'atcay'

vowels_list = ['a', 'e', 'i', 'o', 'u']
punctuation_list = ['!', '?', '.', ';', ':', '\'', '"', '_', '-']

english_sentence = input('Insert a sentence: ')

english_sentence_list = english_sentence.split()

pig_latin_sentence_list = []

#print('testing', english_sentence_list)
#print('testing', pig_latin_sentence_list)

print('*-' * 5)

for word in english_sentence_list:

    word_final_punctuation = ""

    english_word_list = list(word)

    if english_word_list[-1] in punctuation_list:
    	word_final_punctuation = english_word_list.pop(-1)

    if len(english_word_list) > 1:

        if english_word_list[0] not in vowels_list and english_word_list[1] not in vowels_list:
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append('ay')

        elif english_word_list[0] in vowels_list:
            english_word_list.append('yay')

        else:
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append('ay')
    
    else:
        if english_word_list[0] in vowels_list:
            english_word_list.append('yay')

        else:
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append('ay')

    pig_latin_word = ''.join(english_word_list)


    pig_latin_word += word_final_punctuation    	

   
    pig_latin_sentence_list.append(pig_latin_word)
    #print('testing', pig_latin_sentence_list)

pig_latin_sentence = ' '.join(pig_latin_sentence_list)

print('Here is your sentence in pig latin:', pig_latin_sentence)
