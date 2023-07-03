from django.contrib import admin  # noqa
from core.models import Category,Author,Book,User,Order,OrderItem

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
