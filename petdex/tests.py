from django.test import TestCase
from .models import Dog, Cat
from .management.commands.seeds import Command
import os

class TestDogSeed(TestCase):

    def setUp(self):
        # Configure the testing database
        self.dog_csv_path = 'dogs.csv'
        with open(self.dog_csv_path, 'w') as file:
            file.write('id,name,temperament,weight,height,life_span,bred_for,image\n')
            file.write('1,Poodle,Active,45-70,10-15,10-18,Hunting,https://cdn2.thedogapi.com/images/SJdJfg5NX.jpg\n')
            file.write('2,Beagle,Friendly,20-25,13-16,10-15,Hunting,https://cdn2.thedogapi.com/images/SJdJfg5NX.jpg\n')
            file.write('3,Poodle,Active,45-70,10-15,10-18,Hunting,https://cdn2.thedogapi.com/images/SJdJfg5NX.jpg\n')

    def tearDown(self):
        # Delete csv file
        os.remove(self.dog_csv_path)
        return super().tearDown()

    def test_seed_dogs(self):
        # seed dogs
        seed_command = Command()
        seed_command.seed_dogs(self.dog_csv_path)
        # check if dogs were created
        self.assertEqual(Dog.objects.count(), 3)
        # check if dogs were created correctly
        dog = Dog.objects.get(id=1)
        self.assertEqual(dog.name, 'Poodle')
        self.assertEqual(dog.temperament, 'Active')
        self.assertEqual(dog.weight, '45-70')
        self.assertEqual(dog.height, '10-15')
        self.assertEqual(dog.life_span, '10-18')
        self.assertEqual(dog.bred_for, 'Hunting')
        self.assertEqual(dog.image, 'https://cdn2.thedogapi.com/images/SJdJfg5NX.jpg')


class TestCatSeed(TestCase):
    
        def setUp(self):
            # Configure the testing database
            self.cat_csv_path = 'cats.csv'
            with open(self.cat_csv_path, 'w') as file:
                file.write('id,name,description,weight,temperament,origin,life_span,adaptability,affection_level,energy_level,health_issues,intelligence,stranger_friendly,child_friendly,hairless,natural,short_legs,rare,indoor,image,wikipedia_url\n')
                file.write('1,Abyssinian,"The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.",3 - 5,"Active, Energetic, Independent, Intelligent, Gentle",Egypt,14 - 15,5,5,5,2,5,5,3,False,True,False,False,False,https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg,https://en.wikipedia.org/wiki/Abyssinian_(cat)\n')
                file.write('2,Aegean,"Native to the Greek islands known as the Cyclades in the Aegean Sea, these are natural cats, meaning they developed without humans getting involved in their breeding. As a breed, Aegean Cats are rare, although they are numerous on their home islands. They are generally friendly toward people and can be excellent cats for families with children.",3 - 5,"Affectionate, Social, Intelligent, Playful, Active",Greece,9 - 12,5,4,3,1,3,4,4,False,False,False,False,False,https://cdn2.thecatapi.com/images/ozEvzdVM-.jpg,https://en.wikipedia.org/wiki/Aegean_cat\n')
                file.write('3,American Bobtail,American Bobtails are loving and incredibly intelligent cats possessing a distinctive wild appearance. They are extremely interactive cats that bond with their human family with great devotion.,3 - 7,"Intelligent, Interactive, Lively, Playful, Sensitive",United States,11 - 15,5,5,3,1,5,3,4,False,False,False,False,False,https://cdn2.thecatapi.com/images/hBXicehMA.jpg,https://en.wikipedia.org/wiki/American_Bobtail\n')
            
        def tearDown(self):
            # Delete csv file
            os.remove(self.cat_csv_path)
            return super().tearDown()

        def test_seed_cats(self):
            # seed cats
            seed_command = Command()
            seed_command.seed_cats(self.cat_csv_path)
            # check if cats were created
            self.assertEqual(Cat.objects.count(), 3)
            # check if cats were created correctly
            cat = Cat.objects.get(id=1)
            self.assertEqual(cat.name, 'Abyssinian')
            self.assertEqual(cat.description, "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.")
            self.assertEqual(cat.weight, '3 - 5')
            self.assertEqual(cat.temperament, 'Active, Energetic, Independent, Intelligent, Gentle')
            self.assertEqual(cat.origin, 'Egypt')
            self.assertEqual(cat.life_span, '14 - 15')
            self.assertEqual(cat.adaptability, 5)
            self.assertEqual(cat.affection_level, 5)
            self.assertEqual(cat.energy_level, 5)
            self.assertEqual(cat.health_issues, 2)
            self.assertEqual(cat.intelligence, 5)
            self.assertEqual(cat.stranger_friendly, 5)
            self.assertEqual(cat.child_friendly, 3)
            self.assertEqual(cat.hairless, False)
            self.assertEqual(cat.natural, True)
            self.assertEqual(cat.short_legs, False)
            self.assertEqual(cat.rare, False)
            self.assertEqual(cat.indoor, False)
            self.assertEqual(cat.image, 'https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg')
            self.assertEqual(cat.wikipedia_url, 'https://en.wikipedia.org/wiki/Abyssinian_(cat)')