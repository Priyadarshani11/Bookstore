from django.test import TestCase
from core.models import Category, Author, Book, User, Order, OrderItem

class ModelTestCase(TestCase):
    def test_category_model(self):
        category = Category.objects.create(name='Category')
        self.assertEqual(str(category), 'Category')

    def test_author_model(self):
        author = Author.objects.create(name='Author')
        self.assertEqual(str(author), 'Author')

    def test_book_model(self):
        author = Author.objects.create(name='Author')
        category = Category.objects.create(name='Category')
        book = Book.objects.create(title='Book', author=author, description='Description', cover_image='path/to/image.jpg', price=9.99, published_date='2023-01-01')
        book.categories.add(category)
        self.assertEqual(str(book), 'Book')

    def test_user_model(self):
        user = User.objects.create(name='User', email='user@example.com', password='password')
        self.assertEqual(str(user), 'User')

    def test_order_model(self):
        user = User.objects.create(name='User', email='user@example.com', password='password')
        order = Order.objects.create(user=user, total_amount=100.00)
        self.assertEqual(str(order), 'Order #1')

    def test_order_item_model(self):
        user = User.objects.create(name='User', email='user@example.com', password='password')
        book = Book.objects.create(title='Book', author=Author.objects.create(name='Author'), description='Description', cover_image='path/to/image.jpg', price=9.99, published_date='2023-01-01')
        order = Order.objects.create(user=user, total_amount=100.00)
        order_item = OrderItem.objects.create(order=order, book=book, quantity=2, price=19.98)
        self.assertEqual(str(order_item), 'Order #1, Book: Book')
