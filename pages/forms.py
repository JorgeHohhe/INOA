from django import forms
from .models import AssetConfiguration

class AssetConfigurationForm(forms.ModelForm):
    class Meta:
        model = AssetConfiguration
        fields = ['asset_name', 'upper_tunnel', 'bottom_tunnel', 'checking_frequency']
