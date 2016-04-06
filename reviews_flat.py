from decimal import Decimal


class Review:

    def __init__(self, user_name, business_name, rating, review_text):
        self.user_name = user_name
        self.business_name = business_name
        self.rating = rating
        self.review_text = review_text

    def __repr__(self):
        return 'Review({}, {}, {}, {})'.format(self.user_name, self.business_name, self.rating, self.review_text)


class Business:
    def __init__(self, business_name):
        self.business_name = business_name

    def __repr__(self):
        """magic repr to format print feature"""
        return 'Business({})'.format(self.business_name)

class User:
    
    def __init__(self, user_name, reviews):
        self.user_name = user_name
        self.reviews = reviews
    def __repr__(self):
        """magic repr to format print feature"""
        return 'User({}, {})'.format(self.user_name, self.reviews)
    
# ********************** END OF CLASSES ****************************
def prompt_for_business_name():
    """ask user for business name, return business name"""
    business_name = input('Business Name:  ')
    return business_name

def format_single_review(review_item):
    """takes in review, instantiate, return instantiated review"""
    single_review = Review(review_item['user_name'], review_item['business_name'], review_item['rating'], review_item['text'])
    return single_review

def formatting_reviews(raw_review_data):
    """takes in list a reviews, reformats and instantiates each list item, returns instantiated
    list"""
    business_reviews = [format_single_review(review_item) for review_item in raw_review_data]
    return business_reviews

def format_single_business(business_item):
    """takes in business item, instantiates, returns instatiated business"""
    single_business = Business(business_item['business_name'])
    return single_business

def formatting_businesses(raw_business_data):
    """takes in raw data, creates a list of businesses and reviews properly instatiated, returns
    list"""
    businesses = {
        business_item['business_name']:format_single_business(
            business_item
            )
        for business_item in raw_business_data
    }
    return businesses

def formatting_user(user_item, reviews):
    """ """
    list_reviews = []
    for review in reviews:
        if review.user_name == user_item['user_name']:
            list_reviews.append(review)

    # list_reviews = [review if user_item['user_name'] in review for review in reviews]
    return User(user_item['user_name'], list_reviews)

def formatting_users(raw_user_data, reviews):
    """ """
    users = [formatting_user(user_item, reviews) for user_item in raw_user_data]

    return users

def create_business_to_reviews(business_and_reviews):
    """takes instatiated list, creates dictionary with business name as key, returns dictionary"""    
    business_to_reviews = {business.business_name:business for business in business_and_reviews}
    return business_to_reviews

def find_avg_rating(search_name):
    """takes reviews fields for business, calc avg on rating, return avg"""



    rating_sum = sum([review.rating for review in self.reviews])
    rating_average = Decimal(rating_sum/len(self.reviews))
    return round((rating_average), 1)

def extract_one_review(self):
    """takes review fields, pulls off one review and corresponding rating for business, return
    one rating"""
    rating = 0
    while rating < 1:
        for review in self.reviews:
            business_review = review
            rating += 1
    return business_review

def main():
    """takes in nothing, lays out the program functions to call, returns nothign"""

    raw_business_data = [
        {
            'business_name': 'Salt & Straw',
        },
        {
            'business_name': 'Voodoo Donuts',
        },
    ]
    raw_user_data = [
        {'user_name': 'Abby'},
        {'user_name': 'Helen'},
        {'user_name': 'Bobby'},
    ]
    raw_review_data = [
        {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 5, 'text': 'Lucious ice cream!'},
        {'user_name': 'Bobby', 'business_name': 'Salt & Straw', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
        {'user_name': 'Abby', 'business_name': 'Salt & Straw', 'rating': 2, 'text': 'Overrated, but I like sugar.'},
        {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
        {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
        {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
    ]

    businesses = formatting_businesses(raw_business_data)
    
    reviews = formatting_reviews(raw_review_data)
    print(reviews)
    users = formatting_users(raw_user_data, reviews)
    
    search_name = prompt_for_business_name()
    result = []
    for item in reviews:
        if item.business_name == search_name:
            result.append(item.rating)
    print(result) 





    



    

    # print(business_to_reviews[search_name].extract_one_review())

    


    #search_name = prompt_for_business_name()

    



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
