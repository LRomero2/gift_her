from django.test import TestCase
from contact.forms import SubscriptionForm, SecureMessageForm


class TestSubscriptionForm(TestCase):
    def test_subscription_form_explicit_fields(self):
        form = SubscriptionForm()

        self.assertEqual(form.Meta.fields, ['email_address'])


class TestSecureMessageForm(TestCase):
    def test_secure_message_form_explicit_fields(self):
        form = SecureMessageForm()

        self.assertEqual(form.Meta.fields, ['name', 'email', 'message'])

    def test_secure_message_required_fields(self):
        form = SecureMessageForm({'name': '', 'email': '', 'message': ''})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(form.errors['email'][0], 'This field is required.')
        self.assertEqual(form.errors['message'][0], 'This field is required.')
