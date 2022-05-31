from django import forms
from interaction.models import Checkout
from interaction.models import Checkout
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class CheckOutForm(forms.ModelForm):
    CHOICES = (
    ('1', _('Drop-off')),
    ('2', _('Pick-up')),
    )
    checkout_choice = forms.ChoiceField(choices=CHOICES, label=_('checkout choice'))
    
    class Meta:
        model = Checkout
        fields = ["checkout_choice"]
        

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(), 
        label="PIN", 
        min_length=6, 
        max_length=6,
    )
        
    class Meta:
        model = User
        fields = ["password"]

    