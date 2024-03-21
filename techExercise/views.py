from django.shortcuts import render, redirect
from .models import TodoList
from .forms import DataInput
from time import sleep

def index_page(request):


    data = TodoList.objects.all()

    if request.method == 'POST':
        form = DataInput(request.POST)

        checked = request.POST.getlist('entry')
        TodoList.objects.filter(itemid__in=checked).delete()

        if form.is_valid():
            item = form.cleaned_data['item']
            if item == '':
                return redirect('/')
            TodoList.objects.create(item=item, itemid=len(TodoList.objects.values_list('item', flat=True))+1)
            return redirect('/')

    else:
        form = DataInput()


    return render(request, 'index.html',{'data': data, 'form': form})
# Create your views here.
