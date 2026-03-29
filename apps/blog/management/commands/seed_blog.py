import random
from django.core.management import BaseCommand
from faker import Faker
from blog.models import Post, Category, Author, Tag

class Command(BaseCommand):
    """
    Seeds the database with sample data
    """
    def handle(self, *args, **kwargs):
        # Ask to remove existing data
        self.remove_data()

        self.stdout.write('Seeding data...')

        # initiate faker
        fake = Faker('pl_PL')

        # Categories
        pre_categories = ['Technologia', 'Podróże', 'Programowanie', 'Kulinaria', 'RPG', 'Planszówki', 'Polityka', 'Rękodzieło']
        categories = []
        for cat in pre_categories:
            category = Category.objects.create(name=cat)
            categories.append(category)

        # New authors!
        authors = []
        for _ in range(10):
            author = Author.objects.create(
                name=fake.name(),
                email=fake.email()
            )
            authors.append(author)

        # Tags
        tags = []
        for _ in range(10):
            tag = Tag.objects.create(
                name=fake.word()
            )
            tags.append(tag)

        
        # Create post
        posts = []
        for _ in range(100):
            post = Post.objects.create(
                title = fake.sentence(nb_words=7),
                content = ' '.join(fake.paragraphs(nb=6)),
                author = random.choice(authors),
                publication_date = fake.date_this_year(),
                category = random.choice(categories)
                )
            posts.append(post)

        # Random Tags for posts
        for p in posts:
            k = random.randint(1,5) 
            selected = random.sample(tags, k=k)
            p.tags.set(selected)

        # Summary
        self.stdout.write(self.style.SUCCESS(f'{len(posts)} posts created in {len(pre_categories)} predefined categories by {len(authors)} authors.'))
        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))



    def remove_data(self):
        posts = Post.objects.all()
        categories = Category.objects.all()
        
        # MESSAGES
        posts_msg = None
        categories_msg = None

        if len(categories) > 0:
            categories_msg = f'{len(categories)} author{"" if len(categories) == 1 else "s"}'
        
        if len(posts) > 0:
            posts_msg = f'{len(posts)} post{"" if len(posts) == 1 else "s"}'

        total = f'There are {categories_msg} {"and" if posts_msg and categories_msg else ""} {posts_msg}.'
        
        # Prompt
        if posts_msg or categories_msg:
            while True:
                self.stdout.write(self.style.NOTICE(f'{total}\nDelete it before creating new ones? [Y/N]'))
                answ = input()
                if answ.lower() == 'y':
                    posts.delete()
                    categories.delete()
                    self.stdout.write(self.style.SUCCESS('Old data removed.'))
                elif answ.lower() == 'n':
                    return
                
        self.stdout.write(self.style.NOTICE('No categories or posts in database.'))