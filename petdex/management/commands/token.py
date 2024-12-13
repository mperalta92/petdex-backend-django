from django.core.management.base import BaseCommand, CommandError
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Creates a token for a given user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username to create a token for')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            token = Token.objects.get(user__username=username)
            print(f"Token for user {username} already exists: {token.key}")
        except Token.DoesNotExist:
            token = Token.objects.create(user__username=username)
            print(f"Token for user {username} created: {token.key}")

