from django.shortcuts import render
from . import logic


def render_index(request):
    print(logic.get_all_flutts())
    # flutt_id = logic.get_id_for_flutt()
    # flutt_user = logic.get_user_name_for_flutt()
    # flutt_text = logic.get_text_for_flutt()
    flutt_return = {
        'flutt_id': flutt_id,
        'flutt_user': flutt_user,
        'flutt_text': flutt_text,
        'date_n_time': date_n_time
    }
    return render(request, 'flutter/index.html', {})
