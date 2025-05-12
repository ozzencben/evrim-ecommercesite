from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Adınız", max_length=100)
    email = forms.EmailField(label="Eposta Adresiniz")
    message = forms.CharField(label="Mesajınız", widget=forms.Textarea)