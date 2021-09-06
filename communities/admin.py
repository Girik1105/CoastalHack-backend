from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.community)
admin.site.register(models.member)
admin.site.register(models.Post)