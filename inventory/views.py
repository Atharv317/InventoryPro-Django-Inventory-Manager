from . import models,form
from .form import ItemForm
from django.shortcuts import render, redirect, get_object_or_404

def item_list(request):
    items = models.Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'inventory/item_form.html', {'form': form})

def edit_item(request, pk):
    item = get_object_or_404(models.Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(models.Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})
