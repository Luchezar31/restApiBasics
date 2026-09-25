from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books_api import views
from books_api.views import PublisherViewSet

router = DefaultRouter()
router.register(r'',PublisherViewSet)

urlpatterns = [
    path('api/book/',include([
        path('',views.BookCreateListApiViewSet.as_view(),name='books'),
        path('<int:pk>/',views.BookDetailApiViewSet.as_view(),name='book')
    ]   
    )),
    path('publisher/',include(router.urls)),
    path('publisher-links/',views.PublisherHyperlinkView.as_view(),name='publisher')
   
] 