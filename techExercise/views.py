from django.shortcuts import render
from .models import TodoList
def index_page(request):
    data = TodoList.objects.all()
    return render(request, 'index.html', {'data': data})
# Create your views here.
