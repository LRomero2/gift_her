from django.shortcuts import render, redirect
from .forms import SecureMessageForm


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

    return render(request, 'contact/contact_us.html', context)


def thankyou_page(request):
    """
    View to render thank you page after visitors send a message
    """
    return render(request, 'contact/thankyou_page.html')


def faqs(request):
    return render(request, 'contact/faqs.html',)


def about(request):
    return render(request, 'contact/about.html',)
