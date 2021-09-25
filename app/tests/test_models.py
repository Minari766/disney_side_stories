# from django.test import TestCase
# from app.models import Post

# class PostModelTests(TestCase):
#     def test_is_empty(self):
#         saved_posts = Post.objects.all()
#         self.assertEqual(saved_posts.count(), 0)

#     def test_is_count_one(self):
#         post = Post(title='test_title', text='test_text')
#         post.save()
#         saved_posts = Post.objects.all()
#         self.assertEqual(saved_posts.count(), 1)

    # def test_saving_and_retrieving_post(self):
    #     post = Post()
    #     title = 'test_title_to_retrieve'
    #     content = 'test_content_to_retrieve'
    #     post.title = title
    #     post.content = content
    #     post.save()

    #     saved_posts = Post.objects.all()
    #     actual_post = saved_posts[0]

    #     self.assertEqual(actual_post.title, title)
    #     self.assertEqual(actual_post.content, text)