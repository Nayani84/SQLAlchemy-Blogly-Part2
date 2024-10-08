"""Seed file to make sample data for blogly db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
spider_man = User(
    first_name="Peter", 
    last_name="Parker", 
    image_url="https://siyahfilmizle.pro/wp-content/uploads/2021/06/Inanilmaz-Orumcek-Adam-2-The-Amazing-Spiderman-2-izle.jpg"
    )
superman = User(
    first_name="Clark",
    last_name="Kent",
    image_url="https://upload.wikimedia.org/wikipedia/en/d/d6/Superman_Man_of_Steel.jpg"
)
batman = User(
    first_name="Bruce",
    last_name="Wayne",
    image_url="https://www.hollywoodreporter.com/wp-content/uploads/2024/05/CAPC_S1_FG_104_00184209_Still300-H-2024.jpg?w=1296&h=730&crop=1"
)
ant_man = User(
    first_name="Scott",
    last_name="Lang",
    image_url="https://tamashiiweb.com/images/item/item_0000014317_qWyNyjX7_01.jpg"
)
wonder_woman = User(
    first_name="Princess",
    last_name="Diana",
    image_url="https://m.media-amazon.com/images/M/MV5BMTYzODQzYjQtNTczNC00MzZhLTg1ZWYtZDUxYmQ3ZTY4NzA1XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg"
)


# Add new objects to session, so they'll persist
db.session.add_all([spider_man,superman,batman,ant_man,wonder_woman])

# Commit--otherwise, this never gets saved!
db.session.commit()


# Add users
Life_Post = Post(
    title="Life", 
    content="Life is like a roller coaster, live it, be happy, enjoy life.", 
    user_id=1
    )
Pets_Post = Post(
    title="Pets", 
    content="A dog will teach you unconditional love. If you can have that in your life, things won't be too bad.", 
    user_id=2
    )
Love_Post = Post(
    title="Love", 
    content="Love is composed of single soul inhabiting two bodies.", 
    user_id=2
    )
Family_Post = Post(
    title="Family", 
    content="Family is not an important thing, It's everything.", 
    user_id=3
    )
Happy_Post = Post(
    title="Happy", 
    content="The purpose of our lives is to be happy.", 
    user_id=4
    )
Sad_Post = Post(
    title="Sad", 
    content="It's ok to be sad.", 
    user_id=5
    )
Education_Post = Post(
    title="Education", 
    content="Education is the key to success.", 
    user_id=5
    )


# Add new objects to session, so they'll persist
db.session.add_all([Life_Post,Pets_Post,Love_Post,Family_Post,Happy_Post,Sad_Post,Education_Post])

# Commit--otherwise, this never gets saved!
db.session.commit()