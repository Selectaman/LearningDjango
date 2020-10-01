# I have created this file
from django.http import HttpResponse

#this will output Hello World
def hello(request):
    return(HttpResponse("Hello World"))