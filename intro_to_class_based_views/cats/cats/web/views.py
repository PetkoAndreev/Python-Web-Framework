from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from cats.web.models import Cat


class IndexView(TemplateView):
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html')


class ShowCatsListView(ListView):
    model = Cat
    template_name = 'cats_list.html'
    context_object_name = 'cats'


def show_cats(request):
    context = {
        'cats': Cat.objects.all(),
    }

    return render(request, 'cats_list.html', context)
