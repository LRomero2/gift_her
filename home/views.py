from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def error_404(request, exception):
    data = {}
    return render(request, 'templates/404.html', data)


def error_500(request,  exception):
    data = {}
    return render(request, 'templates/500.html', data)


def error_403(request,  exception):
    data = {}
    return render(request, 'templates/403.html', data)