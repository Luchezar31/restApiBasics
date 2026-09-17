

from django.urls import include, path

from books_api import views




urlpatterns = [
    path('api/book/',include([
        path('<int:pk>/',views.book,name='book')
    ]
         
    ))
   
]