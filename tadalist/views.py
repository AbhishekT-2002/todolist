from django.shortcuts import render
from .models import tadalist

# Create your views here.
def index(request):
    todo_items = tadalist.objects.order_by('id')
    context = {'todo_items': todo_items}
    return render(request, 'tadalist/index.html', context)