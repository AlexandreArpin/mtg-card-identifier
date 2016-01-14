from django import forms


class UploadImageForm(forms.Form):
    image = forms.FileField()
