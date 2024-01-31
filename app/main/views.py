from django.shortcuts import render
from .models import Data

# Create your views here.
def Home(request):
    context = {
        'data' : Data.objects.all().order_by('Total'),
    }
    return render(request, 'index.html', context)

