import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def shortcode_creator(inst, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    class_name = inst.__class__
    code_exists = class_name.objects.filter(short_code=new_code).exists()
    if code_exists:
        return shortcode_creator(size=size)
    else:
        return new_code
