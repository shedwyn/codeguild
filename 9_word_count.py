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

def dwnld_book_into_text_lines_list():#could be made input so to limit the number scanned
    with open('Pygmalion_stripped.txt') as raw_book_file:
    # Pygmalion_stripped or A_Modest_Proposal_stripped.txt
        book_as_line_strings = raw_book_file.readlines()
    return book_as_line_strings

def prompt_for_task_direction():
    """asks user which Word Count task they wish to do.  returns answer"""
    task_to_do = input('Would you like to \n\
        A) Get a list of individual word counts, \n\
        B) Get a list of word pair counts, \n\
        C) Find the probability of a word or pair of words appearing in this text, \n\
        D) Exit?\n\
        Answer:    ').upper()
    return task_to_do

def begin_end_program():
    """takes in nothing.  directs to start separate tasks.  ends program with goodbye message"""
    print('Word Count and Probability Program Assignment.  Erin Fough.  March 2016')
    
    individual_word_strings = produce_individual_word_strings()
    paired_word_strings = create_paired_word_strings(individual_word_strings)


    task_to_do = 'E' 

    while task_to_do != 'D':

        task_to_do = prompt_for_task_direction()
        launch_programs_or_return(task_to_do)
    
    print('Thank you.  Goodbye.')

def launch_programs_or_return(task_to_do):
    if task_to_do == 'A':
        find_individual_word_count()
    elif task_to_do == 'B':
        find_paired_word_count()
    elif task_to_do == 'C':
        find_probability()
    elif task_to_do == 'D':
    #     print('\nlaunch programs choice d start'.upper(), task_to_do, '\n')
        task_to_do = prompt_confirm_end_program()
    #     print('launch programs choice d final', task_to_do)
    print('launch programs final answer'.upper(), task_to_do, '\n')
    return task_to_do

def prompt_confirm_end_program():
    """takes in nothing, prompts user to confirm ending program.  returns correct end or continue command""" 
    # task_to_do = input('Do you really want to quit?  Y or N?     ').upper()
    # if task_to_do == 'Y':
    #     task_to_do = 'D'

    # elif task_to_do == 'N':
    #     task_to_do = 'E'

    # else:
    #     print('Sorry, I didn\'t understand your answer, the question required Y or N only')
    #     task_to_do = 'E'

    # print('prompt confirm end program', task_to_do)
    return task_to_do

def produce_individual_word_strings():
    """takes in nothing.  generates list of text words as string.  returns list."""
    book_as_line_strings = dwnld_book_into_text_lines_list()
    text_as_single_string = ' '.join(book_as_line_strings)
    text_as_single_words_list = text_as_single_string.split() #for word in text_words_raw
    list_of_text_words_without_punctuation = clean_unneccesary_non_alpha_char(text_as_single_words_list)
    individual_word_strings = list_of_text_words_without_punctuation

    return individual_word_strings

#lookup zip()

def clean_unneccesary_non_alpha_char(text_as_single_words_list):
    """takes in list of single words, strips elements that are stand alone carriage returns.  returns
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
    word_without_punc = text_word.strip('.!,:;?_-()')
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
    """takes in list of words. creates pairs and saves to new list.  returns new list"""
    front_index = 0
    end_point = len(list_of_text_words) - 1
    paired_word_strings_list = []

    for word in range(0, end_point):
        paired_words = list_of_text_words[front_index] + " " + list_of_text_words[front_index + 1]
        paired_word_strings_list.append(paired_words)
        front_index += 1
    return paired_word_strings_list


def create_counting_dictionary(individual_word_strings): 
    """takes in list of word strings, returns dictionary of word/pairs and their corresponding
    frequency in the book.  This function was first developed with single words in mind, hence
    references in the singular case."""
    #with user input, would need to accept result from function that takes that input
    #and converts into appropriate list - pairs, single, phrases, whatever
    word_to_count_dict = {}
    for word in individual_word_strings:
        if word not in word_to_count_dict:
            word_to_count_dict[word] = 1
        elif word in word_to_count_dict:
            word_to_count_dict[word] += 1
            #name, number = line_string.split()        
    return word_to_count_dict 


def prompt_user_for_number_to_rank():
    """asks user for number of rankings to return.  returns input."""
    rank_input = input('How many words/word pairs would you like to list on your ranking list? \n')
    if rank_input == "":
        print('\n\n\n\nYou want the whole list?  Oooooookay....\n\n\n\n')
    print('\n', '\n')
    return rank_input


def sort_word_to_count_dicts(word_to_count_dict):
    """takes in the dict, sorts on key.  returns keys sorted list"""
    sorted_word_to_count_dicts = sorted(
        word_to_count_dict, 
        key=word_to_count_dict.get, 
        reverse=True
        )
    # print('sorted words', len(sorted_word_to_count_dicts))
    return sorted_word_to_count_dicts

def create_ranking_sentences_list_loop(number_to_rank, word_to_count_dict, sorted_word_to_count_dicts):
    """takes in 3 inputs, creates ranked sentences list up to the index indicated.  returns list"""
    index_for_ranking = number_to_rank
    rank_count = 1
    #number_to_rank = number_to_rank
    ranked_sentences_list = []
    for word in sorted_word_to_count_dicts[0:index_for_ranking]:
        word_count = word_to_count_dict[word]
        uppercase_word = word.upper()
        ranked_sentence = uppercase_word + ' is ranked ' + str(rank_count) + ' with ' + str(word_count) + ' occurances.'
        ranked_sentences_list.append(ranked_sentence)
        rank_count += 1
    return ranked_sentences_list


def create_ranking_sentences_list(word_to_count_dict):
    """returns list of sentences with rank and counts"""
    rank_input = prompt_user_for_number_to_rank()
    if rank_input == "":
        blank_rank_input = len(word_to_count_dict)
        rank_input = str(blank_rank_input)
    number_to_rank = int(rank_input)
    sorted_word_to_count_dicts = sort_word_to_count_dicts(word_to_count_dict)
    ranked_sentences_list = create_ranking_sentences_list_loop(number_to_rank, word_to_count_dict, sorted_word_to_count_dicts)

    return ranked_sentences_list



def print_final_ranking(words_ranked_numerically):
    """takes ranking list and reconfigures to nicer output and then prints the list"""
    rank_index = 0  
    for sentence in words_ranked_numerically:
        print(
        '* ' , words_ranked_numerically[rank_index]
        )
        rank_index += 1
    return words_ranked_numerically


def find_individual_word_count():
    """takes in nothing, loads book file, finds the individual word counts, prints, returns list"""
    print('\n\nCounting Individual Words and Ranking the Most Frequent\n\n'.upper())
    individual_word_strings = produce_individual_word_strings()
    word_to_count_dict = create_counting_dictionary(individual_word_strings)
    words_ranked_numerically = create_ranking_sentences_list(word_to_count_dict)
    print_final_ranking(words_ranked_numerically)
    return words_ranked_numerically






def find_paired_word_count():
    """takes in nothing, loads book file, finds the individual word counts, prints, returns list"""
    print('\n\nCounting Pairs of Words and Ranking the Most Frequent\n\n'.upper())
    individual_word_strings = produce_individual_word_strings()
    paired_word_strings = create_paired_word_strings(individual_word_strings)
    word_to_count_dict = create_counting_dictionary(paired_word_strings)
    words_ranked_numerically = create_ranking_sentences_list(word_to_count_dict)
    print_final_ranking(words_ranked_numerically)
    return words_ranked_numerically

def prompt_for_probability_words():
    """takes in nothing, asks user for word or pairs to find probability"""
    probability_words = input('What word(s) would you like to look up?\n')
    print('\n')
    return probability_words

def find_probability():
    """takes in nothing, loads book file, finds the probability of individual or paired words in file.  prints probability,
    returns nothing"""
    print(
        '\n\nFinding Probability for Words or Word-pairs\n\n'.upper(),
        'This feature will give the probability (as a percentage) that the',
        'words(s) you choose will appear in the assigned book/text'
        )
    individual_word_strings = produce_individual_word_strings()
    paired_word_strings = create_paired_word_strings(individual_word_strings)

    #probability_words = 'begin'

    #while probability_words != False:

    probability_words = prompt_for_probability_words()

    if probability_words not in individual_word_strings:
        print('Sorry, that word is not even in the book!  Try again')
        probability_words = prompt_for_probability_words()

    while probability_words in individual_word_strings:

        if ' ' in probability_words:
            word_to_count_dict = create_counting_dictionary(paired_word_strings)

            # words_ranked_numerically = create_ranking_sentences_list(word_to_count_dict)

        elif ' ' not in probability_words:
            word_to_count_dict = create_counting_dictionary(individual_word_strings)

        total_num_items_in_list = len(word_to_count_dict)
        num_probability_words_in_book = word_to_count_dict[probability_words]
        probability_of_word_in_book = num_probability_words_in_book / total_num_items_in_list

    # if num_probability_words_in_book == False:
        # print('That/those words are not in the book, sorry.  Try again.') 

    print(
        'word:', probability_words,
        '\n total in dict:', total_num_items_in_list,
        '\n total num of word in dict:', num_probability_words_in_book,
        '\n probability:', probability_of_word_in_book
        )
    alpha = -1

    return alpha




    



###################CODE##############################
###################CODE##############################
###################CODE#############################

#find_individual_word_count()
#find_paired_word_count()
find_probability()


# book_as_line_strings = dwnld_book_into_text_lines_list()

# list_of_text_words = convert_lines_into_single_words(book_as_line_strings)

# dict_of_count_to_word = create_counting_dictionary(list_of_text_words)

# print_final_ranking(dict_of_count_to_word)

    ################removed experiements#####################
    ################removed experiements#####################
    ################removed experiements#####################

def old_code_holding_tank():
    x = "old code holding tank"


    # def pair_words_loop(list_of_text_words):
    # #     """takes in list of strings.  runs for loop into new list.  returns new list"""
    # #     front_index = 0
    # #     back_index = 1
    # #     paired_word_strings_list = []
    # #     for word[front_index] in list_of_text_words
    # #         paired_words = " ".join(list_of_text_words[front_index:back_index]).upper().split()
    # #         paired_word_strings_list.append(paired_words)
    # #         front_index += 1
    # #         back_index += 1
    # #     return paired_word_strings_list



    # text_words_without_punctuation = strip_specific_char_from_word(text_lines_list)
    # book_list_without_creturns = clean_unneccesary_non-alpha_char(text_words_without_punctuation)
    # list_of_text_words = convert_lines_into_single_words(book_list_without_creturns)

    #dict_of_count_to_word = convert_word_strings_into_counting_dict(text_lines_list)

    # ranked_sentences_list = create_ranking_sentences_list(dict_of_count_to_word)

    # print_final_ranking(ranked_sentences_list)



   



    # testing_text = 'I will type out a set of sentences. This will help divide us into a list.  I should store \
    # # this somewhere as a module.  A module of variables.  That might be a good idea.  I am not sure.  I will just \
    # # keep typing until I have enough.  This is annoying?'

    # testing_single_word = strip_specific_char_from_word('!beladona,')

    # testing_words_list = ['module.', '!elevator.', 'good', 'annoying?']


    # max_word = max(dict_of_count_to_word, key=dict_of_count_to_word.get)
    # max_word_value = dict_of_count_to_word[max_word]
    # combined_word_val_sentence = 'rank' + '  ' + 'is' + max_word + 'at' + str(max_word_value)



    # dict_of_count_to_word_pairs = sorted(dict_of_count_to_word.items())
    # for value in dict_of_count_to_word_pairs:
    #     #reverse appearance from word, count to count, word
    #     print(value.slice[1])
    # dict_of_count_to_word_pairs['a']

    # print(dict_of_count_to_word_pairs)

    #combined_rank_val_list = create_combined_rank_word_val_list(dict_of_count_to_word)
       

    #print(combined_rank_val_list)






    # def create_rank_word_val_sentence(max_word, max_word_value, ranking):
    #     """ returns sentence """
    #     combined_word_val_sentence = '# {} - {} with {} appearances'.format(ranking, max_word, max_word_value)
    #     return combined_word_val_sentence

    # def find_next_max_word_count_on_max_key(dict_of_count_to_word, max_word):
    #     """takes in most recent max_word and sets new value to 0.  returns new dict"""
    #     max_word = max(dict_of_count_to_word, key=dict_of_count_to_word.get)
    #     return max_word

    # def change_max_val_in_dict_of_count_to_word(dict_of_count_to_word, max_word):
    #     dict_of_count_to_word[max_word] = 0
    #     return dict_of_count_to_word

    # def create_combined_rank_word_val_list(dict_of_count_to_word):
    #     ranking = 1
    #     ranking_tally = 10 #could make this an input
    #     combined_rank_word_val = []
    #     true_max_word = max(dict_of_count_to_word, key=dict_of_count_to_word.get)
    #     max_word = true_max_word
    #     while ranking_tally > 0:
    #         dict_of_count_to_word = change_max_val_in_dict_of_count_to_word(dict_of_count_to_word)
    #         max_word_value = dict_of_count_to_word[max_word]#printing correctly
    #         combined_word_val_sentence = create_rank_word_val_sentence(
    #             max_word, 
    #             max_word_value, 
    #             ranking, 
    #             )
    #         #because max_word not chaninging, this is wrong
    #         combined_rank_word_val.append(combined_word_val_sentence)
    #         #wrong
    #         dict_of_count_to_word = change_max_val_in_dict_of_count_to_word(dict_of_count_to_word, max_word)
    #         max_word = find_next_max_word_count_on_max_key(dict_of_count_to_word, max_word)#try returning \
    #             #word instead of list here
    #         print(dict_of_count_to_word)#this updated only first item
    #         ranking_tally -= 1
    #         ranking += 1
    #     return combined_rank_word_val




    # def convert_word_strings_into_counting_dict(list_of_text_words):
    #     """take in list of words, make dict where keyvalue = unique word and
    #     valueofkey = tally of keys"""
    #     dict_of_count_to_word = {}
    #     for word in list_of_text_words:
    #         if word not in dict_of_count_to_word:
    #             dict_of_count_to_word[word] = 1
    #         elif word in dict_of_count_to_word:
    #             dict_of_count_to_word[word] += 1
    #             #name, number = line_string.split()
    #     return dict_of_count_to_word

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
    return x
###################END OLD CODE ZONE##########################
