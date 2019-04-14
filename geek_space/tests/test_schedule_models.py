from geek_space.models.note import Note
from geek_space.models.user import User
from geek_space.tests.base import BaseTestClass


class TestUserModel(BaseTestClass):

    def test_save_note(self, db):
        user = User(username='test_user', email='test@example.com', password='password')
        note = Note(title='note test user', content='Content test note', user_id=user.id)
        db.session.add(user)
        db.session.add(note)
        db.session.commit()
        check_note = Note.query.filter_by(title=note.title).first()
        assert note == check_note
        assert note.user_id == check_note.user_id

    def test_delete_note(self, db):
        note = Note.query.first()
        db.session.delete(note)
        db.session.commit()
        delete_note = Note.query.filter_by(title=note.title).first()
        assert delete_note is None
