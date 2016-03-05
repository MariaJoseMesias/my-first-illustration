from django.shortcuts import render
from django.utils import timezone
from .models import Illustration

def illustration_list(request):
    illustrations = Illustration.objects.order_by('published_date')
    return render(request, 'pepaillustration/illustration_list.html', {'illustrations': illustrations})