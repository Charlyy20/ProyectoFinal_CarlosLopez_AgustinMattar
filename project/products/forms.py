from django import forms
from . import models
    
class LlantaCreateForm(forms.ModelForm):
    class Meta:
        model = models.Llanta
        fields = "__all__"
        widgets = {
        
        }
        
class AleronCreateForm(forms.ModelForm):
    class Meta:
        model = models.Aleron
        fields = "__all__"
        widgets = {
            
        }
        
class SpoilerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Spoiler
        fields = "__all__"
        widgets = {
            
        }
        
class IntakeCreateForm(forms.ModelForm):
    class Meta:
        model = models.Intake
        fields = "__all__"
        widgets = {
            
        }
        
class WidebodyCreateForm(forms.ModelForm):
    class Meta:
        model = models.Widebody
        fields = "__all__"
        widgets = {
            
        }