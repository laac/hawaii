from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    context = {
        'classInicio': 'current-menu-ancestor'
    }
    return render(request,"index.html",context)

def contact_view(request,*args, **kwargs):
    context = {
        'classContacto': 'current-menu-ancestor'
    }
    return render(request,"contact.html",context)

def about_view(request,*args, **kwargs):
    context = {
        'classAbout': 'current-menu-ancestor'
    }
    return render(request,"about.html",context)

def productos_view(request,*args, **kwargs):
    context = {
        'classProductos': 'current-menu-ancestor'
    }
    return render(request,"products.html",context)

def blog_view(request,*args, **kwargs):
    context = {
        'classBlog': 'current-menu-ancestor'
    }
    return render(request,"blog.html",context)