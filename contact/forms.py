from django import forms


class EmailForm(forms.Form):
    firstname = forms.CharField(label="Vorname", max_length=255)
    lastname = forms.CharField(label="Nachname", max_length=255)
    email = forms.EmailField(label="E-Mail")
    subject = forms.CharField(label="Betreff", max_length=255)
    message = forms.CharField(label="Deine Nachricht", widget=forms.Textarea)
