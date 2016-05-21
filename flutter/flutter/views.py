from django.http import HttpResponse
from django.shortcuts import render
from . import logic


def render_index(request):
    """renders a page with 10 recent flutts, connections to add and search"""
    flutts = logic.get_ten_flutts()
    context = {
        'flutts': flutts
    }
    return render(request, 'flutter/index.html', context)


def render_add_flutt(request):
    """renders form to add flutt, link to home page, and submit button"""
    return render(request, 'flutter/add_flutt.html', {})


def render_post_submit(request):
    """renders acknowledgement of adding new flutt with link """
    # If I want to default value, need a new logic.py function
    # to deal with blank returns
    new_user = request.POST['new_user']
    new_text = request.POST['new_text']
    new_flutt = logic.create_and_save_new_flutt(new_user, new_text)
    context = {
        'new_user': new_flutt.user,
        'new_text': new_flutt.text,
        'new_date': new_flutt.date_n_time
    }
    return render(request, 'flutter/acceptance.html', context)


def render_search_page(request, text):
    """elbow grease"""
    print(text)
    flutts = logic.find_search_text_flutts(text)
    return render(request, 'flutter/index.html', context)


def render_user_flutt_page(request, flutt_user):
    """shows (up to) 10 flutts for indicated user"""
    flutts = logic.get_ten_user_flutts(flutt_user)
    context = {
        'flutts': flutts
    }
    return render(request, 'flutter/user_flutts.html', context)
