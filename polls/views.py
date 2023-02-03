from django.http import HttpResponse


def index(request):
    return HttpResponse("Here would be flashcards application")