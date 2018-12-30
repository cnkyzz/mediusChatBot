from django.test import TestCase
from .models import User
from . import consumers

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Julia")

    def test_user_name(self):
        user = User.objects.get(name="Julia")
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)

    def test_user_isSmoker(self):
        user = User.objects.get(name="Julia")
        self.assertEqual(user.smoker, False)

    def test_user_index(self):
        user = User.objects.get(name="Julia")
        self.assertEqual(user.answerIndex, 1)
