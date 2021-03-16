from .forms import SubscriptionForm


def subscription_form(request):
    sub_form = SubscriptionForm()
    context = {'sub_form': sub_form}
    return context