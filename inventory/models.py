from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    # Link each item to a specific user (so each user sees only their own inventory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Item details
    name = models.CharField(max_length=100)  # Name of the item
    quantity = models.IntegerField()  # Current stock quantity
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item
    category = models.CharField(max_length=50)  # Category (e.g., Electronics, Grocery, etc.)

    # If stock falls below this number, it will be marked as low stock
    low_stock_threshold = models.IntegerField(default=5)

    def __str__(self):
        # How the item will be displayed in Django admin and other places
        return self.name

    @property
    def is_low_stock(self):
        # Returns True if the quantity is less than or equal to the threshold
        return self.quantity <= self.low_stock_threshold
