from django.contrib import admin
from .models import Album, Person, City, Career, Track

admin.site.register(Person)
admin.site.register(City)
admin.site.register(Career)
admin.site.register(Album)
admin.site.register(Track)