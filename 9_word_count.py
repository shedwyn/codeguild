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
    book_as_lines.remove('\n')
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



def tally_up_subfunction():
    """  """



###################CODE##############################

with open('A_Modest_Proposal_stripped.txt') as raw_book_file:
    book_as_lines = raw_book_file.readlines()


unique_word_counts = convert_word_strings_into_counting_dict(book_as_lines)





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



