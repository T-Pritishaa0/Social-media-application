from django.contrib import admin
from . import models as post_models
admin.site.register(post_models.Post)
admin.site.register(post_models.Comment)
# Register your models here.
