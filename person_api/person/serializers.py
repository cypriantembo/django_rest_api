from rest_framework import serializers
from .models import Career, City, Person, Album


class PersonSerializer(serializers.ModelSerializer):
    #date_of_birth = serializers.DateField(input_formats=['%Y-%m-%d']) #only request for the date part alone

    #SRF will force our api to render the actual name of a related resource rather than the id of the resource
    #SRF will query the table and give us actual resource name and SRF is writeable
    career = serializers.SlugRelatedField( 
        many=True,
        slug_field='area_of_study',
        queryset=Career.objects.all())

    city = serializers.SlugRelatedField( 
        many=False,
        slug_field='city',
        queryset=City.objects.all())

    class Meta:
        model = Person
        fields = ['id', 'name', 'gender', 'date_of_birth', 'career', 'city', 'url']

class CitySerializer(serializers.ModelSerializer):
    #validators, func name has to be validate, iexact ignores case when validating
    def validate(self, data):
        if City.objects.filter(city__iexact=data['city']).exists():
            raise serializers.ValidationError(f"{data['city']} already exists")
        return data

    class Meta:
        model = City
        fields = ['id', 'city', 'url']

   

class CareerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Career
        fields = ['id', 'area_of_study', 'url']




class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']