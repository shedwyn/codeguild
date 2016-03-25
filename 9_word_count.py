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
    #while ranking >= 1:
    for word in unique_words_sorted:
        word_count = unique_word_counts[word]
        uppercase_word = word.upper()
        ranked_sentence = uppercase_word + ' is ranked ' + str(ranking) + ' with ' + str(word_count) + ' occurances.'
        ranked_sentences_list.append(ranked_sentence)
        ranking += 1
    return ranked_sentences_list
  
def print_ranking_strings_list(ranked_sentences_list):
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

with open('A_Modest_Proposal_stripped.txt') as raw_book_file:
    book_as_lines = raw_book_file.readlines()


unique_word_counts = convert_word_strings_into_counting_dict(book_as_lines)

# unique_word_counts = {
#     'a':20, 'the': 25, 'an':14, 'of':28, 'duck':10, 
#     'go':16, 'he':20, 'she':4, 'eel':5, 'Weird Al': 8,
#     'goat':15, 'xylophone':1
#     }

ranked_sentences_list = create_ranking_sentences_list(unique_word_counts)

print_ranking_strings_list(ranked_sentences_list)


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





################removed experiements#####################

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

