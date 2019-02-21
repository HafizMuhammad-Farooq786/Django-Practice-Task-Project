from django.urls import path
from . import views

urlpatterns = [
    # path('', views.new_index, name='new_index'),
    # path('dic/', views.dic, name='dictionary'),
    path('index/', views.main, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/gallerypage', views.gallerypage, name='gallerypage'),
    path('blog/', views.blog, name='blog'),
    path('blog/blognextpage/', views.blognextpage, name='blognextpage'),
    path('contact/', views.contact, name='contact'),
]