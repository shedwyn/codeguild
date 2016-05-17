from django.http import HttpResponse


from . import logic


def render_word_count_page(request):
    """renders page requesting word from user"""
    # response = HttpResponse(status=200)
    word_to_find = request.GET['word']
    count_of_word = logic.find_count_for_word_in_book(
        word_to_find, word_to_counts
    )
    return HttpResponse(word_to_find + ' : ' + str(count_of_word), status=200)
    # return response.write(
    #     word_to_find + ' occurs ' + str(count_of_word) +
    #     ' times in A Modest Proposal by Jonathan Swift'
    # )
# move this into logic:
word_to_counts = logic.create_counting_dictionary()
