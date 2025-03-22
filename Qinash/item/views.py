from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Item, Category
from .forms import NewItemForm, EditItemForm

# Create your views here.

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)


    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(request, pk):
    """ Items detail view """
    item = get_object_or_404(Item, pk=pk)
    related_items =Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item':item,
        'related_items':related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        # Initialize the form with the submitted data
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form but don't commit to the database yet
            item = form.save(commit=False)
            # Set the created_by field to the current user
            item.created_by = request.user
            # Now save the item to the database
            item.save()
            # Redirect to the item's detail page
            return redirect('item:detail', pk=item.id)
    else:
        # Initialize an empty form for GET requests
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',  # Update the title to reflect that this is for creating a new item
    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
        
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
