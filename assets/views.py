from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, AssetCategory
from .forms import AssetForm  # make sure you have this!

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'assets/asset_list.html', {'assets': assets})

def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'assets/asset_form.html', {'form': form})

def asset_update(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'assets/asset_form.html', {'form': form})

def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'assets/asset_confirm_delete.html', {'asset': asset})
