from django.shortcuts import render
from .models import Promise

def promise_list(request):
    promises = Promise.objects.all()
    return render(request, 'promises/promise_list.html', {'promises': promises})

