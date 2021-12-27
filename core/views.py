from django.shortcuts import render, HttpResponse
# RENDER é para renderizar na PAG
# HttpResponse é o que faz mostrar na PAG

# Create your views here.


def hello(request, nome, idade):
    # request é uma requisição
    # TODOS OS PARAMETROS SE ENCONTRAM NA URL DO HELLO_DJANGO
    return HttpResponse('<h1>Hello World! {}, você tem {} anos</h1>'.format(nome, idade))
# É possivel usar as tags HTML em parametros por conta do HTTP response

def soma(request, n1, n2):
    resultado = n1 + n2
    return HttpResponse('A soma entre {} e {} é {}'.format(n1, n2, resultado))


def subtracao(request, n1, n2):
    resultado = n1 - n2
    return HttpResponse('A subtração entre {} e {} é {}'.format(n1, n2, resultado))


def multiplicacao(request, n1, n2):
    resultado= n1 * n2
    return HttpResponse('A multiplicação entre {} e {} é {}'.format(n1, n2, resultado))


def divisao(request, n1, n2):
    resultado= n1/ n2
    return HttpResponse('A divisisão entre {} e {} é {}'.format(n1, n2, resultado))