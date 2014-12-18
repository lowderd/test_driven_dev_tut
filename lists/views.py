from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item


# Home page
def home_page(request):

    # Only save if an item has been entered
    if request.method == 'POST':
        # Save item
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world')

    return render(request, 'home.html')


# List view
def view_list(request):

    items = Item.objects.all()

    return render(request, 'list.html', {'items': items})
