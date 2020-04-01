from django import forms

class ContactForm(forms.Form):
    name =    forms.CharField(widget=forms.TextInput(attrs={'name':'name', 'id':'name', 'class':'form-control', 'type':'text'}))
    email =   forms.EmailField(widget=forms.TextInput(attrs={'name':'email', 'id':'email', 'class':'form-control', 'type':'text'}) )
    subject = forms.CharField(required=True,max_length=500, widget=forms.TextInput(attrs={'name':'subject', 'id':'subject', 'class':'form-control', 'type':'text'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'name':'message', 'id':'message', 'class':'form-control'}))