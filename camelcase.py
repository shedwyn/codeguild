import re


def request_initial_word():
    """request and return user snake_cased word"""
    return input('\nsnake_case word please:  ')


def transform_snake_to_camel(word):
    """take word and return it as CamelCase"""
    return ''.join([_.capitalize() for _ in user_word.split('_')])


def transform_camel_to_snake(word):
    """take CamelCase word and return it in snake_case"""
    split_word = re.findall('[A-Z][^A-Z]*', camel_cased_user_word)
    return '_'.join(word.lower() for word in split_word)


def main():
    """collection of functions for program"""
    snake_word = request_initial_word()
    camel_word = transform_snake_to_camel(snake_word)
    snake_word2 = transform_camel_to_snake(camel_word)

    print('\n The CamelCase version of your word is:  ', camel_word)
    print('\n The snake_case version of your word is:  ', snake_word2)

    # split_camel_case_word = list(camel_cased_user_word)

    # print(split_camel_case_word)

    # snake_cased_camel_word = '_'.join(word.lower() for word in split_camel_case_word)

    # print(snake_cased_camel_word)

if __name__ == __main__:
    main()
