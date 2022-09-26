from django.shortcuts import render

from rest_framework import viewsets, permissions, filters, authentication
from .models import Album, Person, City, Career
from .serializers import PersonSerializer, CitySerializer, CareerSerializer, AlbumSerializer
# from person.authentication import TokenAuthentication

class PersonView(viewsets.ModelViewSet): 
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # authentication_classes = [TokenAuthentication] #using bearer 
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # view level -> only authenticated users willl be able to PUT
    #perform a related lookup on a ForeignKey or ManyToManyField with the lookup API double-underscore notation:
    #career is model rel name, area_of_study is actual field name
    filterset_fields = ["name", 'city__city', 'career__area_of_study'] # http://127.0.0.1:8000/person/?name=Peter&city=Lusaka
    # http://127.0.0.1:8000/person/?name=Peter&city__city=Ndola&career=HR, evertthing is case sensitive
    

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CareerView(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['area_of_study']
    #http://127.0.0.1:8000/career/?search=admin or http://127.0.0.1:8000/career/?search=Admin

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer