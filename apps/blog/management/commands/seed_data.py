import random
from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Author, Post # Załóżmy, że mamy takie modele


class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    
    def handle(self, *args, **kwargs):
        self.remove_data()
        
        self.stdout.write('Seeding data...')
        
        # Inicjalizujemy Faker
        fake = Faker('pl_PL') # Używamy polskiego wariantu

        # Stwórzmy 10 autorów
        authors = []
        for _ in range(10):
            author = Author.objects.create(
                name=fake.name(),
                email=fake.email()
        )
            authors.append(author)

        self.stdout.write(self.style.SUCCESS(f'{len(authors)} authors created.'))
        # Stwórzmy 50 postów
        posts = []
        for _ in range(50):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=' '.join(fake.paragraphs(nb=5)),
                author=random.choice(authors), # Losowy autor z listy
                publication_date=fake.date_time_this_year()
        )
            posts.append(post)

        self.stdout.write(self.style.SUCCESS(f'{len(posts)} posts created.'))
        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))

    def remove_data(self):
        posts = Post.objects.all()
        authors = Author.objects.all()
        
        # MESSAGES
        posts_msg = None
        authors_msg = None

        if len(authors) > 0:
            authors_msg = f'{len(authors)} author{"" if len(authors) == 1 else "s"}'
        
        if len(posts) > 0:
            posts_msg = f'{len(posts)} post{"" if len(posts) == 1 else "s"}'

        total = f'There are {authors_msg} {"and" if posts_msg and authors_msg else ""} {posts_msg}.'
        
        # Prompt
        if posts_msg or authors_msg:
            while True:
                self.stdout.write(self.style.NOTICE(f'{total}\nDelete it before creating new ones? [Y/N]'))
                answ = input()
                if answ.lower() == 'y':
                    posts.delete()
                    authors.delete()
                    self.stdout.write(self.style.SUCCESS('Old data removed.'))
                elif answ.lower() == 'n':
                    return
                
        self.stdout.write(self.style.NOTICE('No authors or posts in database.'))