from django.contrib import admin
from .models import User

# registering models for admin panel
admin.site.register(User)