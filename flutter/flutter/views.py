from django.http import HttpResponse
from django.shortcuts import render
from . import logic


def render_index(request):
    flutts = logic.get_all_flutts()
    fill_data = {
        'flutts': flutts
    }
    return render(request, 'flutter/index.html', fill_data)


def render_add_flutt(request):
    return render(request, 'flutter/add_flutt.html', {})


def render_post_submit(request):
    """renders page flutt"""
    new_user = request.POST['new_user']
    new_text = request.POST['new_text']
    new_flutt = logic.create_and_save_new_flutt(new_user, new_text)
    context = {
        'new_user': new_user,
        'new_text': new_text,
        'new_flutt': new_flutt.date_n_time
    }
    return render(request, 'flutter/acceptance.html', context)
