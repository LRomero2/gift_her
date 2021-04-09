from django.test import TestCase
from contact.models import Subscription, SecureMessage


class TestContactModels(TestCase):

    def setUp(self):

        SecureMessage.objects.create(
            name='Mr Test',
            email='test@test.com',
            message='test secure message'
        )

    def test_subscription_str_method(self):
        new_subscription = Subscription.objects.create(
            email_address='test@test.com'
        )

        self.assertEqual(str(new_subscription), 'test@test.com')

    def test_secure_message_str_method(self):
        new_secure_message = SecureMessage.objects.get(name='Mr Test')

        self.assertEqual(str(new_secure_message), 'Mr Test')

    def tearDown(self):
        new_secure_message = SecureMessage.objects.get(name='Mr Test')

        del new_secure_message
