from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from contact.models import Subscription
from contact.forms import SecureMessageForm


class TestContactViews(TestCase):

    def test_new_subscription_email_and_redirect(self):
        response = self.client.post(reverse('subscribe'),
                                    data={
                                        'email_address': 'test@test.com',
                                        'subscribe_redirect': '/'})
        messages = list(get_messages(response.wsgi_request))
        expected_message = 'You are now subscribed to our newsletter.'

        self.assertRedirects(response, '/')
        self.assertEqual(str(messages[0]), expected_message)

    def test_existing_subscription_email_and_redirect(self):
        Subscription.objects.create(
            email_address='test@test.com'
        )
        response = self.client.post(reverse('subscribe'),
                                    data={
                                        'email_address': 'test@test.com',
                                        'subscribe_redirect': '/'})
        messages = list(get_messages(response.wsgi_request))
        expected_message = 'You are already subscribed to our newsletter.'

        self.assertRedirects(response, '/')
        self.assertEqual(str(messages[0]), expected_message)

    def test_secure_message_view(self):
        response = self.client.get('/contact_us/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')

    def test_secure_message_form_submit_and_redirect(self):
        data = {
            'name': 'Mr Test',
            'email': 'test@test.com',
            'message': 'test secure message'
        }
        form = SecureMessageForm(data)
        response = self.client.post(reverse('contact_us'), data, follow=True)
        messages = list(get_messages(response.wsgi_request))
        expected_message = ('Your message has been received'
                            + ' and we aim to reply within 48 hours.')

        self.assertTrue(form.is_valid())
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)
        self.assertRedirects(response, '/')

    def test_faqs_view(self):
        response = self.client.get('/contact/faqs/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/faqs.html')

    def test_about_view(self):
        response = self.client.get('/contact/about/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/about.html')