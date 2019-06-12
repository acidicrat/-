from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth import authenticate, login


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text

class register_form(UserCreationForm):
    class meta:
        model = User
        fields = ('username','email')



class login_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def get_user(self):
        return self.user or None

    def clean(self):
        cleaned_data = super(login_form, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'],
                                password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Неправильный логин или пароль')
            self.user = user
        return cleaned_data
    


# Create your models here.
