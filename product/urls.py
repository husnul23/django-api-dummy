from django.urls import include, path
from .views import ProductDetail, ProductList

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>/', ProductDetail.as_view(), name='retrieve-product'),
]
