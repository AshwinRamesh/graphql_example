from django.core.management.base import BaseCommand, CommandError
from ...schema import schema

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        query = """
            query {
                users (id: 1){
                    firstName
                    lastName
                    age
                }

            }
        """
        r = schema.execute(query, context_value={
            'data_loader':{
                2: {'id': 1,
                    'first_name': 'YenDingo',
                    'last_name': 'AshAndrew',
                    'age': 999
                    }
            }
        })
        print(r.data, r.errors)
