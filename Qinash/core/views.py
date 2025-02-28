from django.shortcuts import render

# Create your views here.

#index page views
def index(request):
    return render(request, 'core/index.html')

#contact page views
def contact(request):
    return render(request, 'core/contact.html')