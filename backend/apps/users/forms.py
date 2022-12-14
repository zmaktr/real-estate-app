from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . models import User

class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        error_class = 'error'

class CustomUserChangeFrom(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        error_class = 'error'