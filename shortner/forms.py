from .validators import validate_url, check_com

class SubmitURL(forms.Form):
     url = forms.CharField(label='Submit URL', validators=[validate_url,check_com])

    
    
    
    
    
    
    
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
