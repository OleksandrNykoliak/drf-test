from django.urls import path

from .views import CustomerView, ManagerView, RealEstateView, RealEstateDetailsView, SellerView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('customers/', CustomerView.as_view(), name='customers'),
    path('managers/', ManagerView.as_view(), name='managers'),
    path('real-estates/', RealEstateView.as_view(), name='real-estates'),
    path('real-estate-details/', RealEstateDetailsView.as_view(), name='real-estate-details'),
    path('sellers/', SellerView.as_view(), name='sellers'),
]
