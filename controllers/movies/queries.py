import graphene

from models.movies.types import MoviesOutputType
from models.movies.movies import Movies

class Query(graphene.ObjectType):
    all_movies = graphene.List(MoviesOutputType)

    movie = graphene.Field(MoviesOutputType, movie_id=graphene.UUID(required=True))


    def resolve_all_movies(self, info, **kwargs):
        return Movies.query.all()
    
    def resolve_movie(self, info, movie_id):
        movie = Movies.query.filter_by(id=movie_id).first()
        return movie
