from django.http import HttpResponse
from django.shortcuts import render


# Home page
def home_page(request):
    return render(request, 'home.html',
                  {'new_item_text': request.POST.get('item_text', '')})
