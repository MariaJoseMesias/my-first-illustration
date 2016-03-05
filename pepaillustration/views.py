from django.shortcuts import render

def illustration_list(request):
    return render(request, 'pepaillustration/illustration_list.html', {})
