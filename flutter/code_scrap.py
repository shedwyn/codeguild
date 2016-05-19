def get_list_of_ids_to_flutts(all_flutts):
    flutts = []
    for flutt in all_flutts:
        flutts.append(
            {
                'id': flutt.id,
                'date': flutt.date_n_time,
                'user': flutt.user,
                'text': flutt.text
            }
        )
    return flutts
