from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()
    
    
        
class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required = False)