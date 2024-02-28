from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

# admin.site.unregister(User)  # нужно что бы снять с регистрации модель User

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = UserCreationForm.Meta.model
#         fields = '__all__'
#         field_classes = UserCreationForm.Meta.field_classes


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom',
            {
                'fields':(
                    'username', 'email', 'filial'
                )
            }
        )
    )
    



admin.site.register(CustomUser, UserAdmin)