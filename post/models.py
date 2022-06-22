from django.db import models
from user.models import Profile
from django.conf import settings

# Post Model
class Post(models.Model):
    owner = models.ForeignKey("user.Profile", on_delete=models.CASCADE, related_name='owner')
    text = models.TextField(null=False)
    links = models.URLField(null=True)
    image = models.ImageField(upload_to='images')
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL)  
    files = models.FileField(upload_to ='uploads/')
    gift = models.IntegerField(default=0)  # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.gift / 100)

    def __str__(self):
        return self.text

    """likes count function"""
    def likes_count(self):
       return self.liked_by.all().count()

class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    report_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    ban_post = models.BooleanField(default=False)


    def __str__(self):
        return str(self.report_creator)





