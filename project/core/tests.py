from django.test import TestCase

from .models import Item


class ItemsTestCase(TestCase):
    def setUp(self):
        Item.objects.create(title="Item1", price=10.0)
        Item.objects.create(title="Item2", price=20.0)

    def test_items_creation(self):
        """Item are correctly created"""
        item1 = Item.objects.get(title="Item1")
        item2 = Item.objects.get(title="Item2")
        self.assertEqual(item1.price, 10.0)
        self.assertEqual(item2.price, 20.0)

    def test_items_str(self):
        """Item __str__ method works correctly"""
        item1 = Item.objects.get(title="Item1")
        self.assertEqual(str(item1), "Item1")
