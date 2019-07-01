from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='İsim', required=True)
    surname = forms.CharField(max_length=50, label='Soyisim', required=True)
    mail = forms.EmailField(max_length=50, label='Mail Adresi', required=True)
    content = forms.CharField(max_length=1000, label='İçerik', required=True)
