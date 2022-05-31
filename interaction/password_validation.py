from re import compile as recompile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PinValidator:
    pin_regex = recompile('\d{6}')

    def validate(self, password, user=None):
        if not self.pin_regex.fullmatch(password):
            raise ValidationError(
                _('Your PIN must contain exactly 6 digit'),
                code='pin_6_digits',   
            )

    def get_help_text(self):
        return _(
            "Your PIN must contain exactly 6 digit"
        )