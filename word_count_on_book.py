#9_word_count
#find a book on projectgutenberg.org - need to be on local drive or have file name relative to folder I am working.  
    #download book into correct folder or use the full path
#1 count how often each unique word is used, then print the most frequent top \
    #10 out with their counts
#2 count how often each unique pair of words is used, then print the most frequent top \
    #10 out with their counts.
   
#3 & 4 redo 1 & 2, print out the probability of each of those words or pairs happening
    #frequency of word/total words (cat appears 100 times, total words = 25,000)
#5 use unique pair probabilities to generate text from the book

#open file and readlines


####################CODE LOGIC NOTES###############################

#for word in book_words:
    #if word not in unique_words_with_count:
        #unique_words_with_count = unique_words_with_count

###################FUNCTIONS#######################################


def prompt_for_task_direction():#NOT IN USE
    """asks user which Word Count task they wish to do.  returns answer"""
    task_to_do = input('Would you like to \n\
        A) Get a list of individual word counts, \n\
        B) Get a list of word pair counts, \n\
        C) Find the probability of a word or pair of words appearing in this text, \n\
        D) Exit?\n\
        Answer:    ').upper()
    return task_to_do        

def prompt_confirm_end_program():#NOT IN USE
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

def begin_end_program():#NOT IN USE
    """takes in nothing.  directs to start separate tasks.  ends program with goodbye message"""
    print('Word Count and Probability Program Assignment.  Erin Fough.  March 2016')
    
    book_as_cleaned_words = break_book_into_cleaned_words()
    paired_word_strings = create_paired_word_strings(book_as_cleaned_words)


    task_to_do = 'E' 

    while task_to_do != 'D':

        task_to_do = prompt_for_task_direction()
        launch_programs_or_return(task_to_do)
    
    print('Thank you.  Goodbye.')

def launch_programs_or_return(task_to_do):#NOT IN USE
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

#lookup zip()
#change minimal

def dwnld_book_into_text_lines_list():#could be made input so to limit the number scanned
    with open('A_Modest_Proposal_stripped.txt') as raw_book_file:
    # Pygmalion_stripped.txt or A_Modest_Proposal_stripped.txt
        book_as_line_strings = raw_book_file.readlines()
    return book_as_line_strings

def strip_specific_char_from_word(text_word):
    """takes in the text_word and strips end and fore punctuation.  returns word_without_punc."""
    word_without_punc = text_word.strip('.!,:;?_-()')
    return word_without_punc
    
def remove_word_punctuation_loop(book_as_words):
    """takes in the list of words, strips punctuation from front and end.  returns
    new list"""
    book_as_words_without_end_punct = []
    for word_with_punct in book_as_words:
        word_without_punct = strip_specific_char_from_word(word_with_punct)
        book_as_words_without_end_punct.append(word_without_punct)
    
    return book_as_words_without_end_punct

def clean_unneccesary_non_alpha_char(book_as_words):
    """takes in list of single words, strips elements that are stand alone carriage returns.  returns
    book_as_words_without_non_alpha_char"""

    book_as_words_without_end_punct = remove_word_punctuation_loop(book_as_words)

    count_of_returns = book_as_words_without_end_punct.count('\n')

    while count_of_returns > 0:

        book_as_words_without_end_punct.remove('\n')
        count_of_returns -= 1

    book_as_words_without_non_alpha_char = book_as_words_without_end_punct

    return book_as_words_without_non_alpha_char

def break_book_into_cleaned_words():
    """takes in nothing.  generates list of text words as string.  returns list."""
    book_as_line_strings = dwnld_book_into_text_lines_list()
    text_as_single_string = ' '.join(book_as_line_strings).upper()
    book_as_words = text_as_single_string.split() #for word in text_words_raw
    book_as_words_without_punctuation = clean_unneccesary_non_alpha_char(book_as_words)
    book_as_cleaned_words = book_as_words_without_punctuation

    return book_as_cleaned_words

def create_paired_word_strings(book_as_cleaned_words):
    """takes in list of words. creates pairs and saves to new list.  returns new list"""
    front_index = 0
    end_point = len(book_as_cleaned_words) - 1
    book_as_paired_words = []

    for word in range(0, end_point):
        paired_words = book_as_cleaned_words[front_index] + " " + book_as_cleaned_words[front_index + 1]
        book_as_paired_words.append(paired_words)
        front_index += 1
    return book_as_paired_words

def create_counting_dictionary(book_as_cleaned_words): 
    """takes in list of word strings, returns dictionary of word/pairs and their corresponding
    frequency in the book.  This function was first developed with single words in mind, hence
    references in the singular case."""
    #with user input, would need to accept result from function that takes that input
    #and converts into appropriate list - pairs, single, phrases, whatever
    word_to_counts = {}
    for word in book_as_cleaned_words:
        if word not in word_to_counts:
            word_to_counts[word] = 1
        elif word in word_to_counts:
            word_to_counts[word] += 1
            #name, number = line_string.split()        
    return word_to_counts 

def prompt_user_for_number_to_rank():
    """asks user for number of rankings to return.  returns input."""
    rank_input = int(input('How many words/word pairs would you like to list on your ranking list? \n'))
    if rank_input == "":
        print('\n\n\n\nYou want the whole list?  Oooooookay....\n\n\n\n')
    print('\n', '\n')
    return rank_input

def sort_word_to_counts(word_to_counts):
    """takes in the dict, sorts on key.  returns keys sorted list"""
    sorted_word_to_counts = sorted(
        word_to_counts, 
        key=word_to_counts.get, 
        reverse=True
    )
    # print('sorted words', len(sorted_word_to_counts))
    return sorted_word_to_counts

def create_ranking_sentences_list_loop(number_to_rank, word_to_counts, sorted_word_to_counts):
    """takes in 3 inputs, creates ranked sentences list up to the index indicated.  returns list"""
    if number_to_rank > len(word_to_counts):
        number_to_rank = len(word_to_counts)

    index_for_ranking = number_to_rank

    rank_count = 1
    #ennumerate()
    #number_to_rank = number_to_rank
    ranked_sentences_list = []
    for word in sorted_word_to_counts[0:index_for_ranking]:
        word_count = word_to_counts[word]
        uppercase_word = word.upper()
        ranked_sentence = uppercase_word + ' is ranked ' + str(rank_count) + ' with ' + str(word_count) + ' occurances.'
        ranked_sentences_list.append(ranked_sentence)
        rank_count += 1
    return ranked_sentences_list

def create_ranking_sentences_list(word_to_counts):
    """returns list of sentences with rank and counts"""
    rank_input = prompt_user_for_number_to_rank()
    if rank_input == "":
        blank_rank_input = len(word_to_counts)
        rank_input = str(blank_rank_input)
    number_to_rank = int(rank_input)
    sorted_word_to_counts = sort_word_to_counts(word_to_counts)
    ranked_sentences_list = create_ranking_sentences_list_loop(number_to_rank, word_to_counts, sorted_word_to_counts)

    return ranked_sentences_list

def print_final_ranking(words_ranked_numerically):
    """takes ranking list and reconfigures to nicer output and then prints the list"""
    rank_index = 0  
    #try ennumerate() = list of two tuples with 2nd item as index from orig list
    for sentence in words_ranked_numerically:
        print(
        '* ' , words_ranked_numerically[rank_index]
        )
        rank_index += 1
    return words_ranked_numerically

def find_individual_word_count():
    """takes in nothing, loads book file, finds the individual word counts, prints, returns list"""
    print('\n\nCounting Individual Words and Ranking the Most Frequent\n\n'.upper())
    book_as_cleaned_words = break_book_into_cleaned_words()
    word_to_counts = create_counting_dictionary(book_as_cleaned_words)
    words_ranked_numerically = create_ranking_sentences_list(word_to_counts)
    print_final_ranking(words_ranked_numerically)
    return words_ranked_numerically

def find_paired_word_count():
    """takes in nothing, loads book file, finds the individual word counts, prints, returns list"""
    print('\n\nCounting Pairs of Words and Ranking the Most Frequent\n\n'.upper())
    book_as_cleaned_words = break_book_into_cleaned_words()
    paired_word_strings = create_paired_word_strings(book_as_cleaned_words)
    word_to_counts = create_counting_dictionary(paired_word_strings)
    words_ranked_numerically = create_ranking_sentences_list(word_to_counts)
    print_final_ranking(words_ranked_numerically)
    return words_ranked_numerically

def prompt_for_pair_or_single_search():
    type_of_search = input("\nAre you looking for a 'pair' or 'single' words?\n")
    return type_of_search

def find_word_in_word_to_counts(word_to_find, word_to_counts):
    while word_to_find not in word_to_counts:
        word_to_find = input('\nWord/pair not available, try again:\n').upper()
    return word_to_find

def prompt_for_word_to_find(word_to_counts):
    """takes in nothing, asks user for word or pairs to find probability"""
    word_to_find = input('What word(s) would you like to look up?\n').upper()
    find_word_in_word_to_counts(word_to_find, word_to_counts)
    print('\n')
    return word_to_find

def calculate_probability_as_float(word_to_counts, word_to_find, count_of_word):
    total_num_words = len(word_to_counts)
    
    probability_as_float = count_of_word / total_num_words
    return probability_as_float

def print_word_and_probability(probability_as_float, word_to_find):
    """takes in float and word.  prints answer string"""
    print('Word Given: ', word_to_find,
        '\n Percentage probability of finding this word in the book: ', round(probability_as_float, 5) * 100,
    )
    return

def find_probability_for_word():
    """takes nothing, loads book file, finds the probability of individual or paired words in 
    file.  returns probability_as_float"""
    print(
        '\n\nFinding Probability for Words or Word-pairs\n\n'.upper(),
        'This feature will give the probability (as a percentage) that the',
        'words(s) you choose will appear in the assigned book/text'
        )
    
    book_as_cleaned_words = break_book_into_cleaned_words()
    type_of_search = prompt_for_pair_or_single_search().upper()

    if type_of_search == 'PAIR':
        paired_word_strings = create_paired_word_strings(book_as_cleaned_words)
        word_to_counts = create_counting_dictionary(paired_word_strings)
    else: 
        type_of_search == 'SINGLE'
        word_to_counts = create_counting_dictionary(book_as_cleaned_words)
    #word_to_counts = word_to_counts
    
    word_to_find = prompt_for_word_to_find(word_to_counts).upper()
    count_of_word = word_to_counts[word_to_find]
    probability_as_float = calculate_probability_as_float(word_to_counts, word_to_find, count_of_word)
    print_word_and_probability(probability_as_float, word_to_find)

    return probability_as_float


###################CODE##############################
###################CODE##############################
###################CODE#############################

find_individual_word_count()
print('\n\n\n')
find_paired_word_count()
print('\n\n\n')
find_probability_for_word()


# book_as_words = convert_lines_into_single_words(book_as_line_strings)

# dict_of_count_to_word = create_counting_dictionary(list_of_text_words)

# print_final_ranking(dict_of_count_to_word)