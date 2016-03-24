#9_word_count
#find a book on projectgutenberg.org - need to be on local drive or have file name relative to folder I am working.  
    #download book into correct folder or use the full path
#1 count how often each unique word is used, then print the most frequent top 10 out with their counts
#2 count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.
    #the cat slept on the couch
    #the cat, cat slept, slept on
#3 & 4 redo 1 & 2, print out the probability of each of those words or pairs happening
    #frequency of word/total words (cat appears 100 times, total words = 25,000)
#5 use unique pair probabilities to generate text from the book


#We will spend an hour on this tomorrow

#open file and readlines

####################CODE LOGIC NOTES###############################

#for word in book_words:
    #if word not in unique_words_with_count:
        #unique_words_with_count = unique_words_with_count

###################FUNCTIONS#######################################

def strip_punctuation(book_as_lines):
    """takes in the book_as_lines and strips end and fore punctuation.  returns book_as_lines."""
    for line in book_as_lines:
        line.strip('.')
        line.strip('\n')
        line.strip('!')
        line.strip(',')
        line.strip(':')
    book_list_without_punc = book_as_lines
    return book_list_without_punc

def remove_carriage_return_lines(book_list_without_punc):
    """takes in book, strips elements that are stand alone carriage returns.  returns
    book_as_lines"""

    count_of_returns = book_list_without_punc.count('\n')
    while count_of_returns > 0:
        book_list_without_punc.remove('\n')
        count_of_returns -= 1
    book_list_without_creturns = book_list_without_punc

    return book_list_without_creturns

def convert_line_strings_into_dict(book_list_without_creturns):
    """takes in corrected book as list of lines, and returns as a list of words"""
    book_as_word_string = ' '.join(book_list_without_creturns)
    book_as_words = list(book_as_word_string.split())

    return book_as_words

def convert_word_strings_into_counting_dict(book_as_lines):
    """take in list of words, make dict where keyvalue = unique word and
    valueofkey = tally of keys"""

    book_list_without_punc = strip_punctuation(book_as_lines)
    book_list_without_creturns = remove_carriage_return_lines(book_list_without_punc)
    book_list_as_words = convert_line_strings_into_dict(book_list_without_creturns)
    #print(book_list_as_words)
    unique_word_counts = {}
    for word in book_list_as_words:
        if word not in unique_word_counts:
            unique_word_counts[word] = 1
        elif word in unique_word_counts:
            unique_word_counts[word] += 1
            #name, number = line_string.split()
    return unique_word_counts
    

def create_rank_word_val_list(unique_word_counts):
    """ returns create_rank_word_val_list """
    max_tally = 10 #could make this an input
    rank = 1
    combined_rank_word_val = []
    while max_tally > 0:
        for word in unique_word_counts:
            max_word = max(unique_word_counts)
            max_word_value = unique_word_counts[max_word]
            unique_word_counts[max_word] = 0
            comb_word_value_sentence = '# {} - {} with {} appearances'.format(rank, max_word, max_word_value)
            combined_rank_word_val.append(comb_word_value_sentence)
            rank += 1
            max_tally -= 1          
    return combined_rank_word_val
    print(combined_rank_word_val)
    
def print_ranking_strings_list(ranked_word_val_list):
    """returns formatted strings list of rankings"""
    print(ranked_word_val_list)


    #top_ten_list = #random_list(:11)

    #word_counts_keys = list(unique_word_counts))




###################CODE##############################

with open('A_Modest_Proposal_stripped.txt') as raw_book_file:
    book_as_lines = raw_book_file.readlines()


unique_word_counts = convert_word_strings_into_counting_dict(book_as_lines)

ranked_word_val_list = create_rank_word_val_list(unique_word_counts)
print_ranking_strings_list(ranked_word_val_list)




################removed experiements#####################

# def convert_word_strings_into_counting_dict(book_as_words):
#     """take in list of words, make dict where keyvalue = unique word and
#     valueofkey = tally of keys"""
#     unique_word_counts = {}
#     for word in book_as_words:
#         if word not in unique_word_counts:
#             unique_word_counts[word] = 1
#         elif word in unique_word_counts:
#             unique_word_counts[word] += 1
#             #name, number = line_string.split()
#     return unique_word_counts

#def other_random_function(book_as_lines):
#     """    """

#     book_list_without_punc = strip_punctuation(book_as_lines)
#     book_list_without_creturns = remove_carriage_return_lines(book_list_without_punc)
#     book_list_as_words = convert_line_strings_into_dict(book_list_without_creturns)
#     #print(book_list_as_words)
#     unique_word_counts = {}
#     for word in book_list_as_words:
#         words_count = book_list_as_words.count(word)
#         word_set = tuple(word,words_count)

