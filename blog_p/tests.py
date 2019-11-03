from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import post

# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                     username = 'testuser',
                     email ='test@email.com',
                     password = 'secret',
        )
        self.post = post.objects.create(
                     title ='A good title',
                     body ='Great content',
                     author = self.user,
        )
    def test_string_representation(self):
        Post = post(title='a sample title')
        self.assertEqual(str(Post), Post.title)

    def test_post_content(self):
        self.assertEqual(self.Post.title,'A good title')
        self.assertEqual(self.Post.author,'testuser')
        self.assertEqual(self.Post.body,'Nice body content')


    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
