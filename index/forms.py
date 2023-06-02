from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    company = forms.CharField(label='Company', max_length=100)
    email = forms.EmailField(label='Email Address')
