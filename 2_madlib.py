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

def madlib(adjective, noun, plural_noun):
	print('There are many {} ways to choose a {} to read.\
        \nFirst you could ask for recommendations from your friends and {}.'.format(adjective, noun, plural_noun))
	return

madlib('green', 'tree', 'cars')