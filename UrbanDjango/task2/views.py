from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index_funk(request):
    return render(request, 'func_template.html')

class index_class(TemplateView):
    template_name = 'class_template.html'