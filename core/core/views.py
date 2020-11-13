from django.http import HttpResponse

def hello(request):
    return HttpResponse('Ola mundo')

#def articles(request, year):
    #return HttpResponse('o ano enviado foi: ' + str(year))    
