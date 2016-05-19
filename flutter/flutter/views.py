from django.shortcuts import render
from . import logic


def render_index(request):
    flutts = logic.get_all_flutts()
    print(flutts)
    fill_data = {
        'flutts': flutts
    }
    return render(request, 'flutter/index.html', fill_data)
