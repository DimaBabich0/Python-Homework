from django import forms

class DemoForm(forms.Form):
  first_name = forms.CharField(label='First name', min_length=2, max_length=30)
  last_name = forms.CharField(label='Last name', min_length=2, max_length=30)