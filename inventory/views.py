from . import models
from .forms import ItemForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


@login_required
def item_list(request):
    # Show only the items that belong to the logged-in user
    items = models.Item.objects.filter(user=request.user)
    return render(request, 'inventory/item_list.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)  # Create object but don't save yet
            item.user = request.user  # Assign the current user to the item
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'inventory/item_form.html', {'form': form})


@login_required
def edit_item(request, pk):
    # Ensure the item exists and belongs to the current user
    item = get_object_or_404(models.Item, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form})


@login_required
def delete_item(request, pk):
    # Ensure the item exists and belongs to the current user
    item = get_object_or_404(models.Item, pk=pk, user=request.user)

    if request.method == 'POST':
        item.delete()
        return redirect('item_list')

    return render(request, 'inventory/item_confirm_delete.html', {'item': item})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log them in immediately
            return redirect('item_list')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/signup.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)  # End the session
    return redirect('login')
