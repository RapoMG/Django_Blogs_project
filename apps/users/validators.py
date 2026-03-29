from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _  # translates error to users language

def validate_username_not_email(value):
    """Reversed validation - don't allow username to be valid email."""
    try:
        validate_email(value)
    except ValidationError: # not email, which is good
        return

    # email validated correctly, which raise error
    raise ValidationError(_("Username cannot be an email address."))  # error to rise and translate if needed
