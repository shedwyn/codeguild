from . import models


def get_all_flutts():
    all_flutts = models.Flutt.objects.all().order_by('date_n_time').reverse()
    return all_flutts


def get_ten_flutts():
    all_flutts = models.Flutt.objects.all().order_by(
        'date_n_time'
    ).reverse()[0:10]
    return all_flutts


def create_and_save_new_flutt(user, text):
    new_flutt = models.Flutt(
        user=user,
        text=text
    )
    new_flutt.save()
    return new_flutt


def get_ten_user_flutts(user):
    flutts = get_all_flutts().filter(user=user)
    limited_flutts = flutts[0:10]
    return limited_flutts


def find_search_text_flutts(text):
    flutts = get_all_flutts()
    print(text)
    matches = []
    print(matches)
    for flutt in flutts:
        if text in flutt.text:
            matches.append(flutt)
    return matches
