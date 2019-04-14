import pytest
from geek_space import app as create_app, db
from geek_space.models.user import User
from geek_space.models.note import Note
from geek_space.conf.config import TestingConfig


class BaseTestClass:

    @pytest.fixture
    def app(self):
        app = create_app()
        app.config.from_object(TestingConfig)
        db.create_all()
        yield app
        db.session.remove()  # looks like db.session.close() would work as well
        db.drop_all()

    @pytest.fixture
    def new_user(self):
            user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
            return user

    @pytest.fixture
    def db(self):
        # Create the database and the database table
        db.create_all()

        # Insert user data
        user1 = User(email='patkennedy79@gmail.com', username='patkennedy', password='FlaskIsAwesome')
        note1 = Note(title='test_note', content='Some text for describe the note', user_id=user1.id)
        user2 = User(email='kennedyfamilyrecipes@gmail.com', username='kennedy', password='PaSsWoRd')
        db.session.add(user1)
        db.session.add(note1)
        db.session.add(user2)

        # Commit the changes for the users
        db.session.commit()

        yield db  # this is where the testing happens!

        db.drop_all()
