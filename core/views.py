from django.shortcuts import redirect, render, HttpResponse
from core.models import Evento
# Create your views here.

#def Evento(Request,evento):
    #return HttpResponse("<h1>O nome do evento é {}</h1>".format(evento))

# def index(request):
#     return redirect('/agenda/')

def Lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

# def hello(Request, nome, idade):
#     return HttpResponse('<h1>hello {}, sua idade é {}</h1>'.format(nome,idade))    