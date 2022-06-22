from django.db import models
from post.models import Post
from user.models import Profile

# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    liked = models.ManyToManyField(Profile, related_name='like')
    file = models.FileField(upload_to='comment_files/')

    def __str__(self):
        return str(self.creator)

    """likes count function"""
    def likes_count(self):
       return self.liked.all().count()


# class Repeat Comment
class RepeatComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    defendant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    like = models.ManyToManyField(Profile, related_name='like_comment')

    def __str__(self):
        return str(self.defendant)

    """likes count function"""
    def likes_count(self):
       return self.like.all().count()

