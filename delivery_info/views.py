from django.shortcuts import render

# Create your views here.


def delivery(request):
    """ A view to return the delivery page """

    return render(request, 'delivery/delivery_info.html')
