from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model


class SnackTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123'
        )

        # Create a Snack object for testing
        self.snack = Snack.objects.create(
            title='Chips',
            purchaser=self.user,
            description='Crispy potato chips'
        )


    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))  # Replace with the correct URL name
        self.assertEqual(response.status_code, 200)  # Check if the response is successful
        self.assertTemplateUsed(response, 'snacks/snack_list.html')  # Ensure the correct template is used


    def test_snack_detail_view(self):
        response = self.client.get(reverse('snack_detail', args=[self.snack.pk]))  # Use the primary key of the snack
        self.assertEqual(response.status_code, 200)  # Successful response
        self.assertTemplateUsed(response, 'snacks/snack_detail.html')  # Correct template
        self.assertContains(response, 'Chips')  # Verify that the snack title is displayed


    def test_snack_create_view(self):
        self.client.login(username='testuser', password='password123')  # Log in the user
        response = self.client.post(reverse('snack_create'), {
            'title': 'Cookies',
            'purchaser': self.user.id,  # Pass the user ID
            'description': 'Delicious chocolate chip cookies'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Snack.objects.filter(title='Cookies').exists())  # Check if the snack was created


    def test_snack_update_view(self):
        self.client.login(username='testuser', password='password123')  # Log in the user
        response = self.client.post(reverse('snack_update', args=[self.snack.pk]), {
            'title': 'Updated Chips',
            'purchaser': self.user.id,
            'description': 'Updated description'
        })
        self.assertEqual(response.status_code, 302)  # Successful update should redirect
        self.snack.refresh_from_db()  # Refresh the snack instance
        self.assertEqual(self.snack.title, 'Updated Chips')  # Verify the update


    def test_snack_delete_view(self):
        self.client.login(username='testuser', password='password123')  # Log in the user
        response = self.client.post(reverse('snack_delete', args=[self.snack.pk]))
        self.assertEqual(response.status_code, 302)  # Check for redirect after deletion
        self.assertFalse(Snack.objects.filter(pk=self.snack.pk).exists())  # Verify the snack is deleted

