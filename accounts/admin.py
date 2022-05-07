from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User, GrupoPermission


admin.site.register(User, auth_admin.UserAdmin)
admin.site.register(GrupoPermission)