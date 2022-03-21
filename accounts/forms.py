from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm


class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Username...'})
        self.fields['email'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Email...'})
        self.fields['password1'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Re-enter password...'})

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Enter Username...'})
        self.fields['password'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Enter Pasword...'})


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Old password...'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control mb-2','placeholder':'New password...'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control mb-2','placeholder':'Confirm new password...'})

