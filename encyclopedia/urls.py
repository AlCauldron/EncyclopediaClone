from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="entry"),
    path('wiki/', views.search, name='filtered'),
    path('newpage/', views.page, name='newpage'),
    path('edit/<str:title>', views.edit, name="edit"),
    path('save/',views.save, name='save'),
    path('random/',views.chaos,name="chaos")
]
