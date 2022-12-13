from django.http import HttpResponse

def index(request):
    return HttpResponse("hello,welcome!")

def play(request):
    return HttpResponse("go and play")

