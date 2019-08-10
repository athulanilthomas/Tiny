from django import forms
from .validators import validate_url, check_com

class SubmitURL(forms.Form):
     url = forms.CharField(label='', 
                           validators=[validate_url,check_com],
                           widget = forms.TextInput(
                           attrs ={
                          "placeholder": "Paste URL here",
                          "id":"email",
                          "name":"email"
                                 }
                          )
                         )
    
    
    # def clean(self):
    #     cleaned_data = super(SubmitURL, self).clean()
    
    # def clean_url(self):
    #     url = self.cleaned_data["url"]
    #     url_validator = URLValidator()

    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Entered URL is Invalid")
        
    #     return url
