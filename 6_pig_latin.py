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

english_sentence = input('Insert a sentence: ')

english_sentence_list = english_sentence.split()

pig_latin_sentence_list = []

#print('testing', english_sentence_list)
#print('testing', pig_latin_sentence_list)

print('*-' * 20)

for word in english_sentence_list:

    english_word_list = list(word)
    #print('testing', english_word_list)

    if english_word_list[0:0] != True:
        if english_word_list[0] not in vowels_list and english_word_list[1] not in vowels_list:
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append('ay')
        #print('testing', english_word_list)

        elif english_word_list[0] in vowels_list:
            english_word_list.append('yay')
        #print('testing', english_word_list)

        else:
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append('ay')
        #print('testing', english_word_list)
    
    else:
        if english_word_list[0] in vowels_list:
            english_word_list.append('yay')
        #print('testing', english_word_list)

        else:
            english_word_list.append(english_word_list.pop(0))
            english_word_list.append('ay')
        #print('testing', english_word_list)


    pig_latin_word = ''.join(english_word_list)
    #print('testing', pig_latin_word)
    pig_latin_sentence_list.append(pig_latin_word)
    #print('testing', pig_latin_sentence_list)

pig_latin_sentence = ' '.join(pig_latin_sentence_list)

print('Here is your sentence in pig latin:', pig_latin_sentence)
