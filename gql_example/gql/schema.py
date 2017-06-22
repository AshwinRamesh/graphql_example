import graphene
from graphene import relay
from types import SimpleNamespace
from . import models


class User(graphene.ObjectType):

    class Meta:
        interfaces = (relay.Node,)
    id = graphene.ID(required=True)
    first_name = graphene.String(description='User first name')
    last_name = graphene.String(description='User last name')
    age = graphene.Int(description='User age')

    @classmethod
    def get_node(cls, id, context, into):
        if id in context['data_loader']:
            x = context['data_loader'][id]
            return SimpleNamespace(**x)
        return models.User.objects.get(id=id)


class Query(graphene.ObjectType):
    users = graphene.Field(User, id=graphene.Int())
    node = relay.Node.Field()

    def resolve_users(self, args, context, info):
        return User.get_node(args['id'], context, info)


schema = graphene.Schema(query=Query)
