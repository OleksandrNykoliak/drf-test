from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customer, Manager, RealEstate, RealEstateDetails, Seller
from rest_framework import permissions, viewsets
from .serializers import ManagerSerializer




class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]


class HomeView(TemplateView):
    template_name = 'base.html'

    
class CustomerView(TemplateView):
    template_name = 'customer.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context
    

class ManagerView(TemplateView):
    template_name = 'manager.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['managers'] = Manager.objects.all()
        return context
    

class RealEstateView(TemplateView):
    template_name = 'real_estate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['real_estates'] = RealEstate.objects.all()
        return context
    

class RealEstateDetailsView(TemplateView):
    template_name = 'real_estate_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['real_estate_details'] = RealEstateDetails.objects.all()
        return context
    

class SellerView(TemplateView):
    template_name = 'seller.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sellers'] = Seller.objects.all()
        return context
