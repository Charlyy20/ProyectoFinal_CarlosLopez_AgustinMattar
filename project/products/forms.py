from django import forms
from .models import Llanta, Aleron, Spoiler, Intake, Widebody

class LlantaCreateForm(forms.ModelForm):
    class Meta:
        model = Llanta
        exclude = ['categoria']

class AleronCreateForm(forms.ModelForm):
    class Meta:
        model = Aleron
        exclude = ['categoria']

class SpoilerCreateForm(forms.ModelForm):
    class Meta:
        model = Spoiler
        exclude = ['categoria']

class IntakeCreateForm(forms.ModelForm):
    class Meta:
        model = Intake
        exclude = ['categoria']

class WidebodyCreateForm(forms.ModelForm):
    class Meta:
        model = Widebody
        exclude = ['categoria']