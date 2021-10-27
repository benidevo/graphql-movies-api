import graphene
from datetime import datetime

from models.movies.types import CreateMoviesInputType, MoviesOutputType, UpdateMoviesInputType
from models.movies.movies import Movies


class CreateMovieMutation(graphene.Mutation):
    class Arguments:
        movie = CreateMoviesInputType(required=True)
    
    ok = graphene.Boolean()
    errors = graphene.String()
    result = graphene.Field(MoviesOutputType)

    def mutate(self, info, movie):
        '''
        Add a new favorite movie
        '''
        new_movie = Movies(**movie)
        new_movie.save()

        result = MoviesOutputType(
            id= new_movie.id,
            title=new_movie.title,
            genre=new_movie.genre,
            year=new_movie.year,
            rating=new_movie.rating,
            created_at=new_movie.created_at,
            updated_at=new_movie.updated_at
        )

        return CreateMovieMutation(ok=True, result=result)


class UpdateMoviesMutation(graphene.Mutation):
    class Arguments:
        id = graphene.UUID(required=True)
        movie = UpdateMoviesInputType(required=True)
    
    ok = graphene.Boolean()
    errors = graphene.String()
    result = graphene.Field(MoviesOutputType)

    def mutate(self, info, id, movie):
        try:
            updated_movie = Movies.find_by_id(id)
        except:
            return UpdateMoviesMutation(ok=False, errors='Internal error while fetching movie')

        if not updated_movie:
            return UpdateMoviesMutation(ok=False, errors='movie with the provided ID does not exist')
        
        title = movie.get('title', None)
        genre = movie.get('genre', None)
        year = movie.get('year', None)
        rating = movie.get('rating', None)

        if title:
            updated_movie.title = title
        if genre:
            updated_movie.genre = genre
        if year:
            updated_movie.year = year
        if rating:
            updated_movie.rating = rating

        if movie:
            updated_movie.updated_at = datetime.now()
        
        updated_movie.save()

        result = MoviesOutputType(
            id= updated_movie.id,
            title=updated_movie.title,
            genre=updated_movie.genre,
            year=updated_movie.year,
            rating=updated_movie.rating,
            created_at=updated_movie.created_at,
            updated_at=updated_movie.updated_at
        )

        return UpdateMoviesMutation(ok=True, result=result)


class DeleteMoviesMutation(graphene.Mutation):
    class Arguments:
        id = graphene.UUID(required=True)
    
    ok = graphene.Boolean()
    errors = graphene.String()
    result = graphene.String()

    def mutate(self, info, id):
        try:
            movie = Movies.find_by_id(id)
        except:
            return DeleteMoviesMutation(ok=False, errors='Internal error while fetching movie')

        if not movie:
            return DeleteMoviesMutation(ok=False, errors='movie with the provided ID does not exist')

        movie.delete() 
        return DeleteMoviesMutation(ok=True, result='Successfully deleted movie')


class Mutation:
    add_movie = CreateMovieMutation.Field()
    update_movie = UpdateMoviesMutation.Field()
    delete_movie = DeleteMoviesMutation.Field()
