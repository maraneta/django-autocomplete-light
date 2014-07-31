from django import forms
import autocomplete_light

from ac_test.models import Ingredient

# class FormulaRow(forms.Form):
#     cas = forms.CharField(max_length=60,required=False)
#     name = forms.CharField(max_length=60,required=False)

class FormulaRow(autocomplete_light.ModelForm):
    class Meta:
        model = Ingredient