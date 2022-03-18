from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>' .format(nome, idade))

def soma (request, numb1, numb2):
    r = numb1 + numb2
    return HttpResponse('<h1>A soma de {} e {} - Resultado é: {} </h1>' .format(numb1, numb2, r))

def sub (request, numb1, numb2):
    r = numb1 - numb2
    return HttpResponse('<h1>A subtração de {} e {} - Resultado é: {} </h1>' .format(numb1, numb2, r))

def div (request, numb1, numb2):
    r = numb1 / numb2
    return HttpResponse('<h1>A divisão de {} e {} - Resultado é: {} </h1>' .format(numb1, numb2, r))

def mult (request, numb1, numb2):
    r = numb1 * numb2
    return HttpResponse('<h1>A multiplicação de {} e {} - Resultado é: {} </h1>' .format(numb1, numb2, r))