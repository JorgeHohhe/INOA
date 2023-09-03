from django.shortcuts import render, redirect
from .models import AssetConfiguration
from .forms import AssetConfigurationForm

def home(request):
    if request.method == 'POST':
        form = AssetConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect back to the configuration page
    else:
        form = AssetConfigurationForm()

    configurations = AssetConfiguration.objects.all()
    return render(request, 'home.html', {'form': form, 'configurations': configurations})
