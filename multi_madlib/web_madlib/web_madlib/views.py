from django.http import HttpResponse

def render_madlib_1(request):
    noun1 = request.GET['first_response']
    noun2 = request.GET['second_response']
    noun3 = request.GET['third_response']
    sentence = "{} hugged {} but not {}".format(noun1, noun2, noun3)
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    request_array = request.GET.
    if noun1 == "":
        return HttpResponse.status
    elif noun2 == "":
        return HttpResponse(response_negative + 'second_response was blank')
    elif noun3 == "":
        return HttpResponse(response_negative + 'third_response was blank')
    else:
        return HttpResponse(response_positive + ' ' + sentence)


def render_madlib_2(request):
    noun1 = request.GET['first_response']
    noun2 = request.GET['second_response']
    noun3 = request.GET['third_response']
    sentence = "{} hugged {} but not {}".format(noun1, noun2, noun3)
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    if noun1 == "":
        return HttpResponse.status
    elif noun2 == "":
        return HttpResponse(response_negative + 'second_response was blank')
    elif noun3 == "":
        return HttpResponse(response_negative + 'third_response was blank')
    else:
        return HttpResponse(response_positive + ' ' + sentence)


def render_madlib_3(request):
    noun1 = request.GET['first_response']
    noun2 = request.GET['second_response']
    noun3 = request.GET['third_response']
    sentence = "{} hugged {} but not {}".format(noun1, noun2, noun3)
    response_positive = "200 OK"
    response_negative = "400 BAD REQUEST "
    if noun1 == "":
        return HttpResponse(response_negative + 'first_response was blank')
    elif noun2 == "":
        return HttpResponse(response_negative + 'second_response was blank')
    elif noun3 == "":
        return HttpResponse(response_negative + 'third_response was blank')
    else:
        return HttpResponse(response_positive + ' ' + sentence)
