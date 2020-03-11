from django.shortcuts import render
from rest_framework import routers
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

router = routers.DefaultRouter()

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_page_size(self, request):
        if self.page_size_query_param:
            page_size = min(int(request.query_params.get(self.page_size_query_param, self.page_size)), self.max_page_size)
        if page_size > 0:
            return page_size
        elif page_size == 0:
            return None
        else:
            pass
        return self.page_size


class ViewBreweries(viewsets.ModelViewSet):
    serializer_class = BreweriesSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Brewery.objects.all()

router.register(r'breweries', ViewBreweries)


class ViewBeer(viewsets.ModelViewSet):
    serializer_class = BeerSerializer
    pagination_class = StandardResultsSetPagination
    queryset = Beer.objects.all()

router.register(r'beer', ViewBeer)
