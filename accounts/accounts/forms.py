from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import firma
from .models import fbf 
from .models import kontrol 
from django.forms import ModelForm, DateInput
from accounts.models import Event, EventMember ,kontrol

class OrderForm(ModelForm):
	class Meta:
		model = firma
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ExampleForm(forms.Form):
	my_date_field = forms.DateField()

class FbfForm(ModelForm):
	class Meta:
		model = fbf
		fields = '__all__'

class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class SignupForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class AddMemberForm(forms.ModelForm):
  class Meta:
    model = EventMember
    fields = ['Personel_Adı']


class PostFilterForm(forms.Form):
  SECME = (('1','ISO9001'),('2','ISO14001'),('3','ISO22000'),('4','ISO27001'))
  secme = forms.CharField(widget=forms.Select(choices=SECME,attrs={'class':'form-control'}))


class KontrolForm(ModelForm):
  class Meta:
    model = kontrol
    widgets = {
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'), 
    }
    exclude = ['user']
   
