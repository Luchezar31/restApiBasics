

from django.urls import include, path

from books_api import views




urlpatterns = [
    path('api/book/',include([
        path('',views.BookCreateListApiViewSet.as_view(),name='books'),
        path('<int:pk>/',views.BookDetailApiViewSet.as_view(),name='book')
    ]   
    ))
   
]