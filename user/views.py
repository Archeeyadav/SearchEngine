from django.shortcuts import render
from rest_framework import viewsets 
from django_filters.rest_framework import DjangoFilterBackend

from .filter import CarListingFilter
from .models import CarListing
from .serializers import CarListingSerializer


class CarListingViewSet(viewsets.ModelViewSet):
    queryset = CarListing.objects.all().order_by('-ppc_score')
    serializer_class = CarListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarListingFilter

def car_listing_search(request):
    if request.method == 'GET':
        # Get query parameters from the URL
        queryset = CarListing.objects.all().order_by('-ppc_score')
        seriliser = CarListingSerializer(queryset, many=True)
 
        return render(request, 'index.html', {'search_results': seriliser.data})
    else:
        return render(request, 'index.html', {'search_results': []})
