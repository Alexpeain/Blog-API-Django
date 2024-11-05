from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="secret",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            content="Nice body content",
        )

    def setUp(self):
        self.client.login(email="test@gmail.com", password="secret")

    def test_post_model(self):
        self.assertEqual(self.post.author.email, "test@gmail.com")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.content, "Nice body content")
        self.assertEqual(str(self.post), "A good title")

    def test_api_viewset(self):
        response = self.client.get(reverse("posts-list"))  # Ensure you use 'posts-list'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, self.post.title)
        
    def test_post_detail_view(self): 
        url = reverse("posts-detail", args=[self.post.id]) # Use 'posts-detail' and post ID 
        response = self.client.get(url) 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertContains(response, self.post.title) 
        self.assertContains(response, self.post.content)
