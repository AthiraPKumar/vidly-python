from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # SELECT * FROM movies_movie

    # Movie.objects.filter(release_year=1984)
    # # SELECT * FROM movies_movie WHERE release_year = 1984

    # Movie.objects.get(id=1)

    # # using list comprehension
    # output = ',' .join([movie.title for movie in movies])

    return render(request, 'movies/index.html', {'movies': movies})

    # return HttpResponse(output)


def detail(request, movie_id):
    # try:
    #     # we can use id or pk(primary key)
    #     movie = Movie.objects.get(pk=movie_id)
    #     # name template based on view function
    #     return render(request, 'movies/detail.html', {'movie': movie})
    #     # return HttpResponse(movie_id)
    # except movie.DoesNotExist:
    #     raise Http404()

    # or
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
