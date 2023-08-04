from django.shortcuts import render , redirect
from item.models import Category, Item
from  .forms import SignupForm

# Create your views here.
def index(request):
    items  = Item.objects.filter(is_sold=False).order_by('-created_at')[:4]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'items': items,
        'categories': categories
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save the user
            form.save()
            # login the user
            # redirect the user to the home page
            return redirect('core:index')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html',{
        'form': form
    })