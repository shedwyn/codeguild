from . import models


def get_all_flutts():
    all_flutts = models.Flutt.objects.all().order_by('date_n_time').reverse()
    return all_flutts
