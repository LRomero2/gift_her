from django.shortcuts import render, redirect, reverse
from .forms import SecureMessageForm
from django.contrib import messages


def thankyou_page(request):
    """
    A view to render thank you page after site visitors send a contact form
    """
    return render(request, 'contact/thankyou_page.html')


def secure_message(request):

    if request.method == 'POST':
        form = SecureMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou_page')

    form = SecureMessageForm()

    context = {
        'form': form,
    }


def faqs(request):
    return render(request, 'contact/faqs.html',)


def about(request):
    return render(request, 'contact/about.html',)
