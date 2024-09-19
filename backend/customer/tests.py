from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Customer


class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('token_obtain_pair')
    
    def test_login_with_valid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
    
    def test_login_with_invalid_credentials(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access', response.data)
    
    def test_login_missing_credentials(self):
        data = {
            'username': 'testuser'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




class CustomerAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        self.customer_url = reverse('create_customer')
    
    def test_create_customer_with_valid_data(self):
        data = {
            'first_name': 'Satish',
            'last_name': 'Kanamala',
            'date_of_birth': '1990-01-01',
            'phone_number': '1234567890'
        }
        response = self.client.post(self.customer_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'Satish')

    def test_create_customer_with_invalid_data(self):
        data = {
            'first_name': '',
            'last_name': '',
            'date_of_birth': '',
            'phone_number': ''
        }
        response = self.client.post(self.customer_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_customer_unauthorized(self):
        self.client.credentials()
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'phone_number': '1234567890'
        }
        response = self.client.post(self.customer_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



