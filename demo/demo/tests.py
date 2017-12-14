from django.test import TestCase, Client
from django.contrib.auth.models import User
import base64


class TestAuthServer(TestCase):

    def setUp(self):
        self.user_joe = User.objects.create_user(
            'joe', 'test1@example.com', '1234',)
        User.objects.filter(pk=self.user_joe.id).update(
            **dict(is_active=True, is_staff=True, is_superuser=True))
        self.user_john = User.objects.create_user(
            'john', 'test2@example.com', '1234',)
        User.objects.filter(pk=self.user_john.id).update(
            **dict(is_active=True, is_staff=False, is_superuser=False))
        self.user_jane = User.objects.create_user(
            'jane', 'test31@example.com', '1234',)
        User.objects.filter(pk=self.user_jane.id).update(
            **dict(is_active=False, is_staff=True, is_superuser=True))
        self.c = Client()

    def create_credentials(self, username, password):
        return ('{}:{}'.format(username, password)).encode('base64').rstrip('\n')

    def user_check(self, user, username, password, status_code):
        creds = '{}:{}'.format(username, password)
        creds = creds.encode("utf8")
        b64creds = base64.b64encode(creds)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + b64creds.decode('utf8'),
        }
        response = self.c.get('/', **auth_headers)
        self.assertEqual(response.status_code, status_code,)

    def test_auth_ok(self):
        self.user_check(self.user_joe, 'joe', '1234', 200)

    def test_auth_not_ok(self):
        self.user_check(self.user_joe, 'joe', '1234a', 401)

    def test_non_staff(self):
        self.user_check(self.user_john, 'john', '1234', 200)

    def test_inactive_user(self):
        self.user_check(self.user_jane, 'jane', '1234', 401)
