from django.shortcuts import render, redirect, reverse
from .models import Subscription
from .forms import SubscriptionForm, SecureMessageForm
from django.contrib import messages


def subscribe(request):

    sub_form = SubscriptionForm()
    subscribe_redirect = request.POST.get('subscribe_redirect')
    if request.method == 'POST':
        sub_form = SubscriptionForm(request.POST)
        if Subscription.objects.filter(
            email_address=request.POST.get('email_address')
        ).exists():
            messages.info(
                request, 'You are already subscribed to our newsletter.')
            return redirect(subscribe_redirect)
        else:
            if sub_form.is_valid():
                sub_form.save()
                messages.success(
                    request, 'You are now subscribed to our newsletter.')
    return redirect(subscribe_redirect)


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


def faqs(request):
    return render(request, 'contact/faqs.html',)


def about(request):
    return render(request, 'contact/about.html',)

