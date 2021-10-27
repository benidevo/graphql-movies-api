import graphene


class MoviesOutputType(graphene.ObjectType):
    id = graphene.String(required=True)
    title = graphene.String(required=True)
    genre = graphene.String()
    year = graphene.Int()
    rating = graphene.Float()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()


class CreateMoviesInputType(graphene.InputObjectType):
    title = graphene.String(required=True)
    genre = graphene.String(required=True)
    year = graphene.Int(required=True)
    rating = graphene.Float(required=True)


class UpdateMoviesInputType(graphene.InputObjectType):
    title = graphene.String()
    genre = graphene.String()
    year = graphene.Int()
    rating = graphene.Float()
