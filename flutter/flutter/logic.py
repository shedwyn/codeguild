from . import models


def get_all_flutts():
    all_flutts = models.Flutt.objects.all().order_by('date_n_time').reverse()[0:10]
    return all_flutts


def create_and_save_new_flutt(user, text):
    new_flutt = models.Flutt(
        user=user,
        text=text
    )
    new_flutt.save()
