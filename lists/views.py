from django.http import HttpResponse


# Home page
def home_page(request):
    return HttpResponse('<html><title>To-Do</title></html>')
