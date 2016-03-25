#9_word_count
#find a book on projectgutenberg.org - need to be on local drive or have file name relative to folder I am working.  
    #download book into correct folder or use the full path
#1 count how often each unique word is used, then print the most frequent top \
    #10 out with their counts
#2 count how often each unique pair of words is used, then print the most frequent top \
    #10 out with their counts.
    #the cat slept on the couch
    #the cat, cat slept, slept on
#3 & 4 redo 1 & 2, print out the probability of each of those words or pairs happening
    #frequency of word/total words (cat appears 100 times, total words = 25,000)
#5 use unique pair probabilities to generate text from the book


#We will spend an hour on this tomorrow

#open file and readlines

####################CODE LOGIC NOTES###############################
####################CODE LOGIC NOTES###############################
####################CODE LOGIC NOTES###############################
####################CODE LOGIC NOTES###############################
####################CODE LOGIC NOTES###############################

#for word in book_words:
    #if word not in unique_words_with_count:
        #unique_words_with_count = unique_words_with_count

###################FUNCTIONS#######################################
###################FUNCTIONS#######################################
###################FUNCTIONS#######################################
###################FUNCTIONS#######################################
###################FUNCTIONS#######################################

def dwnld_book_into_text_lines_list(entry):#could be made input so to limit the number scanned
    with open('A_Modest_Proposal_stripped.txt') as raw_book_file:
        text_lines_list = raw_book_file.readlines(entry)
    return text_lines_list



def convert_lines_into_single_words(text_lines_list):
    """takes in corrected book as list of lines, and returns as a list of words"""
    #book_as_word_string = ' '.join(book_list_without_creturns).upper()
    text_as_single_string = ' '.join(text_lines_list)
    text_as_single_words_list = text_as_single_string.split() #for word in text_words_raw

    list_of_text_words_without_punctuation = clean_unneccesary_non_alpha_char(text_as_single_words_list)


    list_of_text_words = list_of_text_words_without_punctuation


    #list_of_text_words = clean_unneccesary_non_alpha_char(text_words_raw_list)
    return list_of_text_words


#lookup zip()

def clean_unneccesary_non_alpha_char(text_as_single_words_list):
    """takes in book, strips elements that are stand alone carriage returns.  returns
    list_of_text_words_without_non_alpha_char"""

    list_of_text_words_without_end_punct = remove_word_punctuation_loop(text_as_single_words_list)

    count_of_returns = list_of_text_words_without_end_punct.count('\n')

    while count_of_returns > 0:

        list_of_text_words_without_end_punct.remove('\n')
        count_of_returns -= 1

    list_of_text_words_without_non_alpha_char = list_of_text_words_without_end_punct



    return list_of_text_words_without_non_alpha_char


def strip_specific_char_from_word(text_word):
    """takes in the text_word and strips end and fore punctuation.  returns word_without_punc."""
    word_without_punc = text_word.strip('.!,:;?_-')
    return word_without_punc
    
def remove_word_punctuation_loop(text_as_single_words_list):
    """takes in the list of words, strips punctuation from front and end.  returns
    new list"""
    list_of_text_words_without_end_punct = []
    for word_with_punct in text_as_single_words_list:
        word_without_punct = strip_specific_char_from_word(word_with_punct)
        list_of_text_words_without_end_punct.append(word_without_punct)
    
    return list_of_text_words_without_end_punct


def create_paired_word_strings(list_of_text_words):

    front_index = 0
    back_index = 1
    paired_word_strings_list = []


    while back_index < len(list_of_text_words):

        paired_words = " ".join(list_of_text_words[front_index:back_index]).upper().split()
        #paired_word_strings_list.append(paired_words)
        front_index += 1
        back_index += 1
    print(paired_word_strings_list)
    return paired_word_strings_list

#Here - List Comprehension probably would be fantastic!

def convert_word_strings_into_counting_dict(list_of_text_words):
    """take in list of words, make dict where keyvalue = unique word and
    valueofkey = tally of keys"""

    text_words_without_punctuation = strip_specific_char_from_word(text_lines_list)
    book_list_without_creturns = clean_unneccesary_non-alpha_char(text_words_without_punctuation)
    list_of_text_words = convert_lines_into_single_words(book_list_without_creturns)
    #print(list_of_text_words)

    #if answer to question is single letter - run 

   
    #Could this have been list comprehension?

def create_counting_dictionary(list_of_text_words): #with user input, 
    #would need to accept result from function that takes that input
    #and converts into appropriate list - pairs, single, phrases, whatever
    unique_word_counts = {}
    for word in list_of_text_words:
        if word not in unique_word_counts:
            unique_word_counts[word] = 1
        elif word in unique_word_counts:
            unique_word_counts[word] += 1
            #name, number = line_string.split()        
    return unique_word_counts 

def create_ranking_sentences_list(unique_word_counts):
    """returns list of sentences with rank and counts"""
    ranking = 1
    # number_of_rankings = int(
    #     input(
    #     'How many top rankings do you want?'
    #     '(10 for Top Ten, 25, for Top Twenty-five, etc): '
    #     ))
    ranked_sentences_list = []
    unique_words_sorted = sorted(
        unique_word_counts, 
        key=unique_word_counts.get, 
        reverse=True
        )
    print(unique_words_sorted) #working fine until this point
    #while ranking >= 1:
    for word in unique_words_sorted:
        word_count = unique_word_counts[word]
        uppercase_word = word.upper()
        ranked_sentence = uppercase_word + ' is ranked ' + str(ranking) + ' with ' + str(word_count) + ' occurances.'
        ranked_sentences_list.append(ranked_sentence)
        ranking += 1
    return ranked_sentences_list
  
def print_final_ranking(ranked_sentences_list):
    """returns formatted strings list of rankings"""
    number_of_rankings = 10 #int(
        #input(
        #'How many top rankings do you want?'
        #'(10 for Top Ten, 25, for Top Twenty-five, etc): '
        #))
    rank_index = 0
    while number_of_rankings != 0:
        print(
        '* ' , ranked_sentences_list[rank_index]
        )
        rank_index += 1
        number_of_rankings -= 1

###################CODE##############################
###################CODE##############################
###################CODE##############################
###################CODE##############################
###################CODE##############################

testing_text = 'I will type out a set of sentences. This will help divide us into a list.  I should store \
this somewhere as a module.  A module of variables.  That might be a good idea.  I am not sure.  I will just \
keep typing until I have enough.  This is annoying?'

testing_single_word = strip_specific_char_from_word('!beladona,')

testing_words_list = ['module.', '!elevator.', 'good', 'annoying?']

text_lines_list = dwnld_book_into_text_lines_list(500)

list_of_text_words = convert_lines_into_single_words(text_lines_list)

dict_word_to_count = create_counting_dictionary(list_of_text_words)

list_of_ranking_sentences = create_ranking_sentences_list(dict_word_to_count)



print(list_of_ranking_sentences)



# text_words_without_punctuation = strip_specific_char_from_word(text_lines_list)
# book_list_without_creturns = clean_unneccesary_non-alpha_char(text_words_without_punctuation)
# list_of_text_words = convert_lines_into_single_words(book_list_without_creturns)

#unique_word_counts = convert_word_strings_into_counting_dict(text_lines_list)

# ranked_sentences_list = create_ranking_sentences_list(unique_word_counts)

# print_final_ranking(ranked_sentences_list)



################removed experiements#####################
################removed experiements#####################
################removed experiements#####################
################removed experiements#####################
################removed experiements#####################
################removed experiements#####################
################removed experiements#####################
################removed experiements#####################


# max_word = max(unique_word_counts, key=unique_word_counts.get)
# max_word_value = unique_word_counts[max_word]
# combined_word_val_sentence = 'rank' + '  ' + 'is' + max_word + 'at' + str(max_word_value)



# unique_word_counts_pairs = sorted(unique_word_counts.items())
# for value in unique_word_counts_pairs:
#     #reverse appearance from word, count to count, word
#     print(value.slice[1])
# unique_word_counts_pairs['a']

# print(unique_word_counts_pairs)

#combined_rank_val_list = create_combined_rank_word_val_list(unique_word_counts)
   

#print(combined_rank_val_list)






# def create_rank_word_val_sentence(max_word, max_word_value, ranking):
#     """ returns sentence """
#     combined_word_val_sentence = '# {} - {} with {} appearances'.format(ranking, max_word, max_word_value)
#     return combined_word_val_sentence

# def find_next_max_word_count_on_max_key(unique_word_counts, max_word):
#     """takes in most recent max_word and sets new value to 0.  returns new dict"""
#     max_word = max(unique_word_counts, key=unique_word_counts.get)
#     return max_word

# def change_max_val_in_unique_word_counts(unique_word_counts, max_word):
#     unique_word_counts[max_word] = 0
#     return unique_word_counts

# def create_combined_rank_word_val_list(unique_word_counts):
#     ranking = 1
#     ranking_tally = 10 #could make this an input
#     combined_rank_word_val = []
#     true_max_word = max(unique_word_counts, key=unique_word_counts.get)
#     max_word = true_max_word
#     while ranking_tally > 0:
#         unique_word_counts = change_max_val_in_unique_word_counts(unique_word_counts)
#         max_word_value = unique_word_counts[max_word]#printing correctly
#         combined_word_val_sentence = create_rank_word_val_sentence(
#             max_word, 
#             max_word_value, 
#             ranking, 
#             )
#         #because max_word not chaninging, this is wrong
#         combined_rank_word_val.append(combined_word_val_sentence)
#         #wrong
#         unique_word_counts = change_max_val_in_unique_word_counts(unique_word_counts, max_word)
#         max_word = find_next_max_word_count_on_max_key(unique_word_counts, max_word)#try returning \
#             #word instead of list here
#         print(unique_word_counts)#this updated only first item
#         ranking_tally -= 1
#         ranking += 1
#     return combined_rank_word_val




# def convert_word_strings_into_counting_dict(list_of_text_words):
#     """take in list of words, make dict where keyvalue = unique word and
#     valueofkey = tally of keys"""
#     unique_word_counts = {}
#     for word in list_of_text_words:
#         if word not in unique_word_counts:
#             unique_word_counts[word] = 1
#         elif word in unique_word_counts:
#             unique_word_counts[word] += 1
#             #name, number = line_string.split()
#     return unique_word_counts

#def other_random_function(text_lines_list):
#     """    """

#     text_words_without_punctuation = strip_specific_char_from_word(text_lines_list)
#     book_list_without_creturns = clean_unneccesary_non-alpha_char(text_words_without_punctuation)
#     list_of_text_words = convert_lines_into_single_words(book_list_without_creturns)
#     #print(list_of_text_words)
#     unique_word_counts = {}
#     for word in list_of_text_words:
#         words_count = list_of_text_words.count(word)
#         word_set = tuple(word,words_count)

