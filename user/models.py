from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from friendship.models import Friend, Follow, Block, FriendshipRequest


# Profile model
class Profile(AbstractUser):
    phone_number = models.CharField(max_length=10)
    github = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    twitter = models.URLField(max_length=200, null=True)
    facebook = models.URLField(max_length=200, null=True)
    profile_image = models.ImageField(upload_to='profile_images')
    friend = models.ManyToManyField(Follow)

    def __str__(self):
        return self.username

# password reset (should be in signals.py)
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}{}".format(('http://localhost:3000/api/password_reset/confirm/'),
                                            reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="from Adda"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
