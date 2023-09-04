import threading
import time
import subprocess

from django.shortcuts import render, redirect
from .models import AssetConfiguration
from .forms import AssetConfigurationForm

# Define global variable
total_configurations = 0


def run_script(asset_name, upper_tunnel, bottom_tunnel, interval_seconds):
    while True:
        # Call your script or function here
        subprocess.run(["python", "stock-quote-alert.py", asset_name, str(upper_tunnel), str(bottom_tunnel)])
        
        # Sleep for the specified interval
        time.sleep(interval_seconds)

def home(request):
    global total_configurations
    if request.method == 'POST':
        form = AssetConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssetConfigurationForm()

    configurations = AssetConfiguration.objects.all()

    if len(configurations) != total_configurations:
        # Get last inserted asset configuration
        last_asset = AssetConfiguration.objects.last()
        total_configurations += 1

        # Change minutes to seconds
        interval_seconds = last_asset.checking_frequency * 60

        # Create a separate thread to run the script
        script_thread = threading.Thread(target=run_script,
            args=(last_asset.asset_name, last_asset.upper_tunnel, last_asset.bottom_tunnel, interval_seconds,)
        )

        # Start the thread
        script_thread.start()

    return render(request, 'home.html', {'form': form, 'configurations': configurations})
