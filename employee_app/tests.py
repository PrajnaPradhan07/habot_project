from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee

class EmployeeAPITests(APITestCase):

    def setUp(self):
        # Create a sample employee for testing
        self.employee = Employee.objects.create(
            name="Test User",
            email="testuser@example.com",
            department="HR",
            role="Manager"
        )
        self.create_url = reverse('employee-list')  # /api/employees/
        self.detail_url = reverse('employee-detail', args=[self.employee.id])  # /api/employees/{id}/

    def test_create_employee(self):
        data = {
            "name": "New User",
            "email": "newuser@example.com",
            "department": "Engineering",
            "role": "Developer"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_with_duplicate_email(self):
        data = {
            "name": "Duplicate User",
            "email": "testuser@example.com",  # already exists
            "department": "Sales",
            "role": "Analyst"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)  # pagination returns 'results'

    def test_retrieve_employee(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test User")

    def test_retrieve_nonexistent_employee(self):
        url = reverse('employee-detail', args=[999])  # non-existent ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        data = {
            "name": "Updated User",
            "email": "testuser@example.com",
            "department": "HR",
            "role": "Manager"
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated User")

    def test_delete_employee(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)