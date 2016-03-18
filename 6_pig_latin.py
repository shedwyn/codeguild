#Pig Latin translator
#enter sentence
#translate to pig latin
#print out

#bonus/advanced - handle vowels with punctuation, punctuation, handle capitalization

#take first letter
#move to end
#add 'ay' on new end

#'cat' - 'atcay'

english_word = input('Insert a word (all lower, no punc): ')

#slice first letter

english_word_list = list(english_word)

vowels_list = ['a', 'e', 'i', 'o', 'u']

if english_word_list[0] not in vowels_list and english_word_list[1] not in vowels_list:
    english_word_list.append(english_word_list.pop(0))
    english_word_list.append(english_word_list.pop(0))
    english_word_list.append('ay')

elif english_word_list[0] in vowels_list:
    english_word_list.append('yay')

else:
    english_word_list.append(english_word_list.pop(0))
    english_word_list.append('ay')

pig_latin_word = ''.join(english_word_list)

print(pig_latin_word)