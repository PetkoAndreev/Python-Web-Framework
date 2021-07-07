from django.shortcuts import render, redirect

from pythons.pythons_app.forms import PythonCreateForm
from pythons.pythons_app.models import Python


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})
