from django.shortcuts import render

# Create your views here.
def index(request) : 
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def new_page_css(request):
    return render (request, 'new_page_css.html')

def baabtra (request):
    return render (request, 'baabtra.html')

def bootstrap (request):
    return render (request, 'bootstrap.html')

def newpage (request):
    return render (request, 'newpage.html')

def bootstrap_grid (request):
    return render (request,'bootstrap_gridsystem.html')
    