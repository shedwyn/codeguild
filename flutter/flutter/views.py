from django.http import HttpResponse
from django.shortcuts import render
from . import logic


def render_index(request):
    """renders a page with 10 recent flutts, connections to add and search"""
    flutts = logic.get_all_flutts()
    fill_data = {
        'flutts': flutts
    }
    return render(request, 'flutter/index.html', fill_data)


def render_add_flutt(request):
    """renders form to add flutt, link to home page, and submit button"""
    return render(request, 'flutter/add_flutt.html', {})


def render_post_submit(request):
    """renders acknowledgement of adding new flutt with link """
    new_user = request.POST['new_user']
    new_text = request.POST['new_text']
    new_flutt = logic.create_and_save_new_flutt(new_user, new_text)
    context = {
        'new_user': new_user,
        'new_text': new_text,
        'new_flutt': new_flutt.date_n_time
    }
    return render(request, 'flutter/acceptance.html', context)


def render_search_page(request):
    """elbow grease"""
    pass
