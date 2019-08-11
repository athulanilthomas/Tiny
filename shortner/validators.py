from django.core.validators import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()
    # reg_val = value
    # if "http" in reg_val:
    #     new_value = reg_val
    # else:
    #     new_value = 'http://' + value
    try:
        url_validator(value)
    except:
        raise ValidationError("Entered URL is Invalid")
    return value

def check_com(value):
    if not ".com" in value:
        raise ValidationError(".com is not present in URL")
    return value
