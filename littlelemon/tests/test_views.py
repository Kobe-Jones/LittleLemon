from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu  # Import your Menu model here
from .serializers import MenuSerializer  # Import your Menu serializer here

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(name="Menu Item 1", description="Description 1", price=10.99)
        self.menu_item2 = Menu.objects.create(name="Menu Item 2", description="Description 2", price=15.99)
        self.menu_item3 = Menu.objects.create(name="Menu Item 3", description="Description 3", price=12.49)

        self.client = APIClient()

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)

        expected_data = MenuSerializer([self.menu_item1, self.menu_item2, self.menu_item3], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, expected_data)
