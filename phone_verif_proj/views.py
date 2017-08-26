from django.http import HttpResponse

def index(request):
    return HttpResponse("<pre>Not found.</pre>")
