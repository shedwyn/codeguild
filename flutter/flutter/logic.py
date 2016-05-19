from . import models


def get_all_flutts():
    flutt_id_to_flutt_data_dict ={}
    for flutt in models.Flutt:
        flutts[models.Flutt.self.flutt.id] = {
            'date': models.Flutt.self.date_n_time,
            'user': models.Flutt.self.flutt_user,
            'text': models.Flutt.self.flutt_text
        }
    return flutts
