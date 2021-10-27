import graphene

from controllers.movies.queries import Query as MoviesQuery
from controllers.movies.mutations import Mutation as MoviesMutation


class Query(MoviesQuery, graphene.ObjectType):
    pass


class Mutation(MoviesMutation, graphene.Mutation):
    
    def mutate(self, info, **kwargs):
        pass
    

schema = graphene.Schema(query=Query, mutation=Mutation)
