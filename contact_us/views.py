from django.shortcuts import render, redirect, reverse
from .models import Subscription
from .forms import SubscriptionForm, SecureMessageForm
from django.contrib import messages


def secure_message(request):

    if request.method == 'POST':
        form = SecureMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ('Your message has been received'
                          + ' and we aim to reply within 48 hours.'))
        return redirect(reverse('home'))

    form = SecureMessageForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact_us.html', context)