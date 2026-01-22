from django.contrib import admin
from .models import Guide,StatusHistory,User
# Register your models here.
admin.site.register(Guide)
admin.site.register(StatusHistory)
admin.site.register(User)