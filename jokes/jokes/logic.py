jokes = [
    {
        'setup': 'Why does Waldo wear stripes?',
        'punchline': 'Because he doesn\'t want to be spotted.'
    },
    {
        'setup': 'I used to have a dog that did magic tricks.',
        'punchline': 'It was a labracadabrador!'
    },
]


def accept_new_joke(joke_setup, joke_punchline):
    """takes in new joke setup and punchline, creates a dict with setup: and
    punchline: and appends jokes list"""
    jokes.append({'setup': joke_setup, 'punchline': joke_punchline})


def get_all_jokes():
    """returns complete list of submitted jokes as list of dicts"""
    return jokes
