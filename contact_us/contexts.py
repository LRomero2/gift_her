from .forms import SecureMessageForm


def SecureMessage_form(request):
    form = SecureMessageForm()
    context = {'form': form}
    return context
