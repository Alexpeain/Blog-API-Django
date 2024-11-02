from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

from .models import Post 

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            email = "test@gmail.com",
            password = "secret",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title = "A good title",
            content = "Nice body content",
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.email,"test@gmail.com")
        self.assertEqual(self.post.title,"A good title")
        self.assertEqual(self.post.content,"Nice body content")
        self.assertEqual(str(self.post), "A good title")