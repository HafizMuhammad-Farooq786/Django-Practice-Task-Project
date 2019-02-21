from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from . import models

# def index(request):
#     return HttpResponse('Hello World! This is my First application view that i have learned how to create this to view')


# def new_index(request):
#     return HttpResponse('Hello World! This is my Second App view that i have learned how to create this to view')


# def dic(request):
#     my_dict = {'insert_me': 'Hello i am from visit'}
#     return render(request, 'index.html', context=my_dict)


def main(request):
    return render(request, 'Home.html')


def about(request):
    return render(request, 'About.html')


def gallery(request):
    return render(request, 'Gallery.html')


def blog(request):
    return render(request, 'Blog.html')


def blognextpage(request):
    return render(request, 'blogNextPage.html')


def gallerypage(request):
    return render(request, 'galleryPage.html')


def contact(request):
    if request.method == 'POST':
        models.Contact(name=request.POST["fname"], email=request.POST['email'], address=request.POST['address'],
                       phone=request.POST['phone'], message=request.POST['message']).save()

        return redirect(main)
    return render(request, 'Contact.html')

