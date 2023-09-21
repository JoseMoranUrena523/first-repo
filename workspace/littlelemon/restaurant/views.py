from rest_framework import generics, viewsets
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]