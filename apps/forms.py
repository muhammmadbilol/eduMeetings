from django import forms


from apps.models import Meet


class ModelForm(forms.ModelForm):
    class Meta:
        model = Meet
        fields = '__all__'

