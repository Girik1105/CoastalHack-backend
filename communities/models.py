from django.db import models

from django.contrib.auth import get_user_model, login
User = get_user_model()

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.utils.text import slugify


# Create your models here.
class community(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    owner = models.ForeignKey(User, related_name='admin', on_delete= models.CASCADE)
    members = models.ManyToManyField(User, through='member')
    cover = models.ImageField(upload_to='uploads/covers', default='uploads/covers/default.jpg', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.name


class member(models.Model):
    community = models.ForeignKey(community, related_name='membership', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name='user_communitys', on_delete = models.CASCADE)
    joined_since = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta():
        unique_together = ('user', 'community')

@receiver(pre_save, sender=community)
def org_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
    
@receiver(post_save, sender=community)
def org_save_member(sender, instance, created, *args, **kwargs):
    if not member.objects.filter(user=instance.owner, community=instance).exists():
        member.objects.create(user=instance.owner, community=instance, is_verified=True)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='community_posts', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/communityposts', blank=True, null=True)
    community = models.ForeignKey(community, related_name='community_posts', null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-timestamp']