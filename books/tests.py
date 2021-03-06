from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User
from django.core import mail


def populate_test_book_data(user=None):
    Book.objects.create(
        title='A Fire Upon the Deep',
        author='Vernor Vinge',
        year=1992,
        user=user
    )
    Book.objects.create(
        title='A Deepness in the Sky',
        author='Vernor Vinge',
        year=1999,
        user=user
    )
    Book.objects.create(
        title='The Children of the Sky',
        author='Vernor Vinge',
        year=2011,
        user=user
    )


class TestBookModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('name', 'email')
        populate_test_book_data(self.user)

    def test_book_data(self):
        one = Book.objects.get(year=1992)
        two = Book.objects.get(year=1999)
        three = Book.objects.get(year=2011)
        self.assertEqual(one.title, 'A Fire Upon the Deep')
        self.assertEqual(two.title, 'A Deepness in the Sky')
        self.assertEqual(three.title, 'The Children of the Sky')
        self.assertEqual(one.author, 'Vernor Vinge')
        self.assertEqual(two.author, one.author)
        self.assertEqual(three.author, two.author)


class TestBookViews(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        self.user = User.objects.create_user('name', 'email')
        populate_test_book_data(self.user)

    def test_book_detail_view(self):
        from .views import book_detail_view
        req = self.request.get('')
        req.user = self.user
        res = book_detail_view(req, f'{ Book.objects.get(year=1992).id }')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'A Fire Upon the Deep', res.content)

    def test_book_detail_404(self):
        from .views import book_detail_view
        from django.http import Http404
        req = self.request.get('')
        req.user = self.user
        with self.assertRaises(Http404):
            book_detail_view(req, '0')

    def test_book_list_view(self):
        from .views import book_list_view
        req = self.request.get('')
        req.user = self.user
        res = book_list_view(req)
        self.assertIn(b'A Fire Upon the Deep', res.content)
        self.assertIn(b'A Deepness in the Sky', res.content)
        self.assertIn(b'The Children of the Sky', res.content)


# class TestClientAuth(TestCase):

#     def test_registration(self):
#         from django_registration.views import RegistrationView
#         self.request = RequestFactory()
#         req = self.request.post(
#             '/accounts/register',
#             data={
#                 'username': 'Milo',
#                 'email': 'milo@test.com',
#                 'password': 'uncommon',
#                 'password2': 'uncommon'
#             }
#         )
#         res = RegistrationView(req)
#         self.assertEqual(len(mail.outbox), 1)
