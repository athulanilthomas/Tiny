import random
import string

def code_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def shortcode_creator(inst, size=6):
    new_code = code_generator(size=size)
    class_name = inst.__class__
    code_exists = class_name.objects.filter(shortcode=new_code).exists()
    if code_exists:
        return shortcode_creator(size=size)
    else:
        return new_code
