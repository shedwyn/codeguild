from decimal import Decimal


class Review:

    def __init__(self, rating, review_text):
        self.rating = rating
        self.review_text = review_text

    def __repr__(self):
        return 'Review({}, {})'.format(self.rating, self.review_text)


class Business:
    def __init__(self, business_name, reviews):
        self.business_name = business_name
        self.reviews = reviews

    def __repr__(self):
        """magic repr to format print feature"""
        return 'Business({}, {})'.format(self.business_name, self.reviews)


    def find_avg_rating(self):
        """takes reviews fields for business, calc avg on rating, return avg"""
        rating_sum = sum([review.rating for review in self.reviews])
        rating_average = Decimal(rating_sum/len(self.reviews))
        return round((rating_average), 1)

    def extract_one_review(self):
        """takes review fields, pulls off one review and corresponding rating for business, return
        one rating"""
        return self.reviews[0]

    
# ********************** END OF CLASSES ****************************
def prompt_for_business_name():
    """ask user for business name, return business name"""
    business_name = input('Business Name:  ')
    return business_name

def format_single_review(review_item):
    """takes in review, instantiate, return instantiated review"""
    single_review = Review(review_item['rating'], review_item['text'])
    return single_review

def formatting_reviews(list_reviews):
    """takes in list a reviews, reformats and instantiates each list item, returns instantiated
    list"""
    business_reviews = [format_single_review(review_item) for review_item in list_reviews]
    return business_reviews

def format_single_business(business_item):
    """takes in business item, instantiates, returns instatiated business"""
    business_reviews = formatting_reviews(business_item['reviews'])
    single_business = Business(business_item['business_name'], business_reviews)
    return single_business

def formatting_businesses(raw_business_review_data):
    """takes in raw data, creates a list of businesses and reviews properly instatiated, returns
    list"""
    business_and_reviews = [
        format_single_business(
            business_item
            )
        for business_item in raw_business_review_data
    ]
    return business_and_reviews

def create_business_to_reviews(business_and_reviews):
    """takes instatiated list, creates dictionary with business name as key, returns dictionary"""    
    business_to_reviews = {business.business_name:business for business in business_and_reviews}
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

    business_and_reviews = formatting_businesses(raw_business_review_data)

    business_to_reviews = create_business_to_reviews(business_and_reviews)

    search_name = prompt_for_business_name()

    average_rating = Business.find_avg_rating(business_to_reviews[search_name])

    print('The average rating for {} was'.format(search_name), average_rating)

    print(Business.extract_one_review(business_to_reviews[search_name]))

    print(business_to_reviews[search_name].extract_one_review())


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
