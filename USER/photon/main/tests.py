from django.test import TestCase
from .models import *
from accounts.models import *
from post.models import * 
# Create your tests here.

class PhotonTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(first_name = "Kinju", last_name = "Shrestha", username="Kinju", email = "Kinju_Shrestha@gmail.com")
        self.post = Post.objects.create(user_id = self.user.id, Title = "NewPost", Caption = "Caption", File="", like=3)
        self.comment = Comment.objects.create(post_id = self.post.id, content = "NewComment")
        # self.user = User.objects.create(username = "kinju", password = "kinju")
    def testUser(self):
        u = User.objects.get(username = "Kinju")
        self.assertEqual(u.username, 'Kinju')

    def testPost(self):
        p = Post.objects.get(user_id = self.user.id)
        self.assertEqual(p.Title, 'NewPost')
    
    def test_Comment(self):
        c = Comment.objects.get(post_id = self.post.id)
        self.assertEqual(c.content, 'NewComment')

    def testPost1(self):
        t = Post.objects.get(user_id = self.user.id)
        self.assertEqual(t.Caption, 'Caption')

    def testPost2(self):
        l = Post.objects.get(user_id = self.user.id)
        self.assertEqual(l.like, 3)
    # def user(self):
    #     response = self.client.post('/login/', self.credentias, follow = True)
    #     self.assertTrue(response.context['user'].is_active)
        
    
