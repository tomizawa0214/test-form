from django.shortcuts import render

def top(request):
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
    return render(request, 'base/top.html', ctx)