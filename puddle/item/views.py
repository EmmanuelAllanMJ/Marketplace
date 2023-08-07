from django.shortcuts import render, get_object_or_404 , redirect
from django.db.models import Q
from item.models import Item, Category 
from django.contrib.auth.decorators import login_required 
from .forms import NewItemForm, EditItemForm

# Create your views here.
def items(request):
    query = request.GET.get('query','')
    catogory_id = request.GET.get('category', 0)
    catogories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) )

    if catogory_id:
        items = items.filter(category_id=catogory_id)
        
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': catogories,
        'category_id': int(catogory_id),
    })


def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[:4]
    return render(request, 'item/details.html',{
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False means don't save to database yet as we want to add the user first
            item = form.save(commit=False) 
            item.created_by = request.user
            item.save()
            return redirect('item:details', pk=item.pk)
    
    form = NewItemForm()
    return render(request, 'item/form.html', {
        'form': form,
        "title" : "New Item"
        })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def newItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item.save()
            return redirect('item:details', pk=item.pk)
    else:
        form = EditItemForm(instance=item)
    return render(request, 'item/form.html', {
        'form': form,
        "title" : "Edit Item"
        })
