from django.http import HttpResponse
from django.shortcuts import render
from . import logic

# jokes = logic.jokes


def render_joke_submission_page(request):
    """render form for submitting new joke"""
    # form.html
    return render(request, 'jokes/form.html', {})


def render_acceptance_page(request):
    """renders page accepting joke to list"""
    joke_setup = request.POST['joke_setup']
    joke_punchline = request.POST['joke_punchline']
    logic.accept_new_joke(joke_setup, joke_punchline)
    context = {
        'joke_setup': joke_setup,
        'joke_punchline': joke_punchline
    }
    # acceptance.html
    return render(request, 'jokes/acceptance.html', context)


def render_joke_list_page(request):
    """render page of jokes already submitted"""
    jokes = logic.get_all_jokes()
    context = {
        'jokes': jokes
    }
    return render(request, 'jokes/list.html', context)  # , jokes)  # , {})
