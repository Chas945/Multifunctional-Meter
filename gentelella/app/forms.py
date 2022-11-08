from django import forms

from .models import Meter, Control

class MeterForm(forms.ModelForm):

    class Meta:

        model = Meter
        fields = '__all__'


class ControlForm(forms.ModelForm):

    class Meta:

        model = Control
        fields = ['control_id', 'name']