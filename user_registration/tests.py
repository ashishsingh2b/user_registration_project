from django.test import TestCase
from django.urls import reverse
from .models import UserProfile
from .forms import UserProfileForm

class RegisterUserViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Optionally set up any data that will be used by all the test methods in this class.
        pass

    def test_register_user_get(self):
        url = reverse('register')
        response = self.client.get(url)

        # Assert that the GET request returns a status code 200 and uses the correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        # Assert that the form in the context is an instance of UserProfileForm
        self.assertIsInstance(response.context['form'], UserProfileForm)

    def test_register_user_post_valid_form(self):
        url = reverse('register')
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'dob': '1990-01-01',
            'hobbies': [],  # Adjust hobbies if needed
            'gender': 'M',
            'address': '123 Test St',
            'remarks': True,
            'email': 'test@example.com',
            'mobile_number': '1234567890',
            'password': 'testpassword',
            'confirm_password': 'testpassword',
        }

        # Send POST request with valid form data
        response = self.client.post(url, form_data)

        # Assert that the POST request redirects to the same page (assuming form handling redirects back on success)
        self.assertEqual(response.status_code, 200)  # Adjust if you expect a different behavior
        self.assertTemplateUsed(response, 'register.html')

        # Optionally check if the user_profile object exists in the context
        self.assertTrue('user_profile' in response.context)

        # Assert that UserProfile object was saved in the database
        self.assertTrue(UserProfile.objects.filter(username='testuser').exists())

    def test_register_user_post_invalid_form(self):
        url = reverse('register')
        form_data = {
            # Invalid form data, missing required fields
            'username': '',
            'first_name': 'Test',
            # Add more fields to test various validation scenarios
        }

        # Send POST request with invalid form data
        response = self.client.post(url, form_data)

        # Assert that the POST request stays on the same page (status code 200) and uses the correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        # Assert that form errors are present in the response
        self.assertFormError(response, 'form', 'username', 'This field is required.')

        # Assert that UserProfile object was not saved in the database
        self.assertFalse(UserProfile.objects.filter(username='').exists())
