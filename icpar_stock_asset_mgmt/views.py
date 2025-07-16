# icpar_stock_asset_mgmt/views.py
from django.shortcuts import render



def home(request):
    return render(request, 'home.html')


def stock_list(request):
    return render(request, 'stock/stock_list.html', {'items': items})
    return render(request, 'stock/stock_form.html', {'form': form})

