class Review:

    def __init__(self, rating, review_text):
        self.rating = rating
        self.review_text = review_text

        return None

    def __str__(self):
        return 'Rating: {}, Text: {}'.format(self.rating, self.review_text)


class Business:

    def __init__(self, business_name, reviews_fields):
        self.business_name = business_name
        self.reviews_fields = reviews_fields

        return None

    def __str__(self):
        """magic string to format print feature"""

        #  CHRIS:  I am thinking we might be able to do this better - unpack and format the list of reviews
            #  into individual lines.  What do you think?

        return 'Business: {}, Reviews {}'.format(self.business_name, self.reviews_fields)

    
# ********************** END OF CLASSES *****************************

# def prompt_for_business_name():
#     """ask user for business name, return business name"""
#     return business_name = input('Business Name:  ')


def format_single_review(review_item):
    
    single_review = Review(review_item['rating'], review_item['text'])
    
    return single_review

def formatting_reviews(list_reviews):
     
    business_reviews = [format_single_review(review_item) for review_item in list_reviews]          

    return business_reviews

def format_single_business(business_item):

    business_reviews = formatting_reviews(business_item['reviews'])
    single_business = Business(business_item['business_name'], business_reviews)

    return single_business

def formatting_businesses(raw_business_review_data):
    
    business_to_reviews = {format_single_business(business_item) for business_item in raw_business_review_data}
            
    return business_to_reviews

def main():
    """takes in nothing, lays out the program functions to call, returns nothign"""

    raw_business_review_data = [
        {
            'business_name': 'Salt & Straw',
            'reviews': [
                {'rating': 5, 'text': 'Lucious ice cream!'},
                {'rating': 4, 'text': 'Super tasty, but such a long line!'},
                {'rating': 2, 'text': 'Overrated, but I like sugar.'}
            ],
        },
        {
            'business_name': 'Voodoo Donuts',
            'reviews': [
                {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
                {'rating': 5, 'text': 'Pink building is so cute!'},
                {'rating': 2, 'text': 'Diabetes inducing.'}
            ]
        }
    ]
    business_to_reviews = formatting_businesses(raw_business_review_data)

    for business_item in business_to_reviews:
        print('\n\n - Business:  ', self.business_name, '\n     Reviews:  ', self.reviews_fields)

    
    
# ********************** END OF DEFINING FUNCTIONS **************************

main()

#  ************     END OF MAIN CALL ZONE ***********************************


# EVERYTHING BELOW IS JUST THE:

# CODE SCRAP HEAP ***********************************************************

# # one_business_dict = {'business_name': 'Salt & Straw', 'reviews': [{'rating': 5, 'text': 'Lucious ice cream!'}, {'rating': 4, 'text': 'Super tasty, but such a long line!'}]}
    

#     reviews = formatting_review(raw_reviews)

#     # single_review = convert_dict_to_review(reviews[0])

# # single_business = Business(one_business_dict['business_name'], [single_review])  # one_business_dict['reviews'])


    
    

# print()
    # business_name = prompt_for_business_name()

