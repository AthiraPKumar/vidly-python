from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.

# RESTFUL API


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  # lazy object
        resource_name = 'movies'  # how our end point would look like
        excludes = ["release_year"]  # things you dont want to be seen in api
