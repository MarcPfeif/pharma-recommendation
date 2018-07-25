from django.http import HttpResponse

def index(request):
    return HttpResponse("Recommendation Engine Default Response")
