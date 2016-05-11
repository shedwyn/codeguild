from django.http import HttpResponse
# from django.shortcuts import render

from . import logic


def render_word_intake_page(request):
    """renders page requesting word from user"""
    response = HttpResponse(status=200)
    word_to_find = request.POST['word']
    # response.write(response_positive + ' ' + sentence)
    return word_to_find


def render_word_count_page(request):
    """renders a page with returned word count from essay by Jonathan Swift"""
    word_to_find = request.POST['word']
    response = HttpResponse(status=200)
    count_of_word = logic.find_count_for_word_in_book(
        word_to_find, word_to_counts
    )
    return word_to_find + ' : ', count_of_word

word_to_counts = logic.create_counting_dictionary()
