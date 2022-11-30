from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, ChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field
from crispy_forms.bootstrap import PrependedText

class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Field(PrependedText('username', '@', placeholder="username")),
      Field('password')
    )

class SignupForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Field(PrependedText('username', '@', placeholder="username")),
      Field('password1'),
      Field('password2')
    )