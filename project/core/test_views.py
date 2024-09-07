from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(title="Test Category")

    def test_list_categories(self):
        url = reverse("category-list")
        response = self.client.get(url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_category(self):
        url = reverse("category-detail", args=[self.category.id])
        response = self.client.get(url)
        category = Category.objects.get(id=self.category.id)
        serializer = CategorySerializer(category)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_category(self):
        url = reverse("category-list")
        data = {"title": "New Category"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(
            Category.objects.get(id=response.data["id"]).title, "New Category"
        )

    def test_premade_category(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().title, "Test Category")

    def test_invalid_retrieve_category(self):
        url = reverse("category-detail", args=[self.category.id + 1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_category(self):
        url = reverse("category-detail", args=[self.category.id])
        data = {"title": "Updated Category"}
        response = self.client.put(url, data)
        self.category.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.category.title, "Updated Category")

    def test_delete_category(self):
        url = reverse("category-detail", args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_partial_update_category(self):
        url = reverse("category-detail", args=[self.category.id])
        data = {"title": "Partially Updated Category"}
        response = self.client.patch(url, data)
        self.category.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.category.title, "Partially Updated Category")

    def test_invalid_create_category(self):
        url = reverse("category-list")
        data = {"title": ""}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 1)

    def test_invalid_update_category(self):
        url = reverse("category-detail", args=[self.category.id])
        data = {"title": ""}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.category.refresh_from_db()
        self.assertNotEqual(self.category.title, "")
