from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Петр',
                                                         'minlength': '2',
                                                         'pattern': '^[А-Я][а-я]+'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'type': 'tel',
               'placeholder': '8(911)123-45-67',
               'pattern': '[0-9]\([0-9]{3}\)[0-9]{3}-[0-9]{2}-[0-9]{2}'}))
