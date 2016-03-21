#make a madlib
#ask for 3 words
#fill in the madlib
#print it out

#adjective, noun, plural noun

#adjective = input("Enter an adjective: ")
#noun = input("Enter a noun:")
#plural_noun = input("Enter a plural noun: ")
#print('- ' * 20)

#print('There are many ' + adjective +
#    ' ways to choose a ' + noun +
#    ' to read.  \nFirst you could ask for recommendations\
#    from your friends and ' + plural_noun)


def prompt_for_adj():
    """prompt the user to give an adjective. return input"""
    print('Give an adjective:\n')
    return input()

def prompt_for_noun():
    """prompt the user to give a noun. return input"""
    print('Give a noun:\n')
    return input()

def prompt_for_pl_noun():
    """prompt the user to give a plural noun. return input"""
    return input('Give a plural noun:\n')

#def prompt_for_adv():
#    print('Give an adverb:\n')
#    return input()

#def prompt_for_verb():
#    print('Give a verb:\n')
#    return input()

def build_madlib(adjective, noun, plural_noun):
    """print a pre-set sentence (included) using the user inputs to fill in the {}"""
    print('There are many {} ways to choose a {} to read.\
        \nFirst you could ask for recommendations from your friends and {}.'.format(adjective, noun, plural_noun))

adject1 = prompt_for_adj()
noun1 = prompt_for_noun()
pl_noun1 = prompt_for_pl_noun()

build_madlib(adject1, noun1, pl_noun1)
