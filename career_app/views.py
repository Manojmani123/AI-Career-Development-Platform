from django.http import HttpResponse

def home(request):
    return HttpResponse("AI Career Development Platform")