from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the homepage. Soon, you can keep track of which movies you've already seen and score them")