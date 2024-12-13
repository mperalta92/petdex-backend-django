from django.core.management.base import BaseCommand, CommandError
from petdex.models import Dog, Cat
import csv

class Command(BaseCommand):
    help = 'Seeds the database with data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='The model to seed data into')

    def handle(self, *args, **kwargs):
        model = kwargs['model']
        if model == 'dog':
            self.seed_dogs('petdex/data_source/dogs.csv')
        elif model == 'cat':
            self.seed_cats('petdex/data_source/cats.csv')
        else:
            raise CommandError(f"Model {model} not found")

    def seed_dogs(self, csv_file_path):
        # read csv file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Dog.objects.create(
                    name=row['name'],
                    temperament=row['temperament'],
                    weight=row['weight'],
                    height=row['height'],
                    life_span=row['life_span'],
                    bred_for=row['bred_for'],
                    image=row['image']
                )
                print(f"Dog {row['id']} created")

    def seed_cats(self, csv_file_path):
        # read csv file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Cat.objects.create(
                    name=row['name'],
                    description=row['description'],
                    weight=row['weight'],
                    temperament=row['temperament'],
                    origin=row['origin'],
                    life_span=row['life_span'],
                    adaptability=row['adaptability'],
                    affection_level=row['affection_level'],
                    energy_level=row['energy_level'],
                    health_issues=row['health_issues'],
                    intelligence=row['intelligence'],
                    stranger_friendly=row['stranger_friendly'],
                    child_friendly=row['child_friendly'],
                    hairless=row['hairless'],
                    natural=row['natural'],
                    short_legs=row['short_legs'],
                    rare=row['rare'],
                    indoor=row['indoor'],
                    image=row['image'],
                    wikipedia_url=row['wikipedia_url']
                )
                print(f"Cat {row['id']} created")