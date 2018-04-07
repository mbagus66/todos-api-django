from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Todos
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
	"""This class defines the test suite for the todos model."""

	def setUp(self):
		"""Define the test client and other test variables."""
		user = User.objects.create(username="faif")
		self.title = "Write world class code"
		# specify owner of a todos
        self.todos = Todos(title=self.title, owner=user)

    def test_model_can_create_a_todos(self):
    	"""Test the todos model can create a todos."""
    	old_count = Todos.objects.count()
        self.todos.save()
        new_count = Todos.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_returns_readable_representation(self):
        """Test a readable string is returned for the model instance."""
        self.assertEqual(str(self.todos), self.title)


class ViewsTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
    	"""Define the test client and other test variables."""
    	user = User.objects.create(username="faif")

    	# Initialize client and force it to use auth
    	self.client = APIClient()
    	self.client.force_authenticate(user=user)

    	# Since user model instance is not serializable, use its Id/PK
    	self.todos_data = {'title': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.todos_data,
            format="json")

    def test_api_can_create_a_todos(self):
        """Test the api has todos creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/todos/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_todos(self):
        """Test the api can get a given todos."""
        todos = Todos.objects.get(id=1)
        response = self.client.get(
            '/todos/',
            kwargs={'pk': todos.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todos)

    def test_api_can_update_todos(self):
        """Test the api can update a given todos."""
        todos = Todos.objects.get()
        change_todos = {'title': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': todos.id}),
            change_todos, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_todos(self):
        """Test the api can delete a todos."""
        todos = Todos.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': todos.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
