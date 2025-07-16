from django.shortcuts import render, redirect, get_object_or_404
from .models import StockItem
from .forms import StockItemForm

def stock_list(request):
    items = StockItem.objects.all()
    return render(request, 'stock/stock_list.html', {'items': items})

def stock_create(request):
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockItemForm()
    return render(request, 'stock/stock_form.html', {'form': form})

def stock_update(request, pk):
    item = get_object_or_404(StockItem, pk=pk)
    if request.method == 'POST':
        form = StockItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockItemForm(instance=item)
    return render(request, 'stock/stock_form.html', {'form': form})

def stock_delete(request, pk):
    item = get_object_or_404(StockItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('stock_list')
    return render(request, 'stock/stock_confirm_delete.html', {'item': item})
