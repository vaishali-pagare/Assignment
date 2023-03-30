from django.contrib import admin
from .models import User,UserImage

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ["id","name","email","password","phone","user"]

admin.site.register(User, AdminUser)

class AdminUserImage(admin.ModelAdmin):
    list_display = ["id","u1","image"]
admin.site.register(UserImage, AdminUserImage)
