from django import forms
from allauth.account.forms import SignupForm


class ProfileForm(forms.Form):
    user_name = forms.CharField(max_length=30, label='ニックネーム')
    icon = forms.ImageField(label='アイコン画像', required=False)

class SignupUserForm(SignupForm):
    user_name = forms.CharField(max_length=30, label='ニックネーム')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.user_name = self.cleaned_data['user_name']
        user.save()
        return user