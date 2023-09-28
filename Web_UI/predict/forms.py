from django import forms
from .models import Predict
class MakePrediction(forms.ModelForm):
    
    class Meta:
        model = Predict
        fields = ["gender","age","hypertension","heart_disease","ever_married",
                  "work_type","Residence_type","avg_glucose_level","bmi","smoking_status","stroke"]
        widgets = {'stroke': forms.HiddenInput()}
