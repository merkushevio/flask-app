from geek_space.models.user import User
from geek_space.tests.base import BaseTestClass


class TestUserModel(BaseTestClass):

    def test_save_username(self, db):
        user2 = User(username='test_user', email='test@example.com', password='password')
        db.session.add(user2)
        db.session.commit()
        check_user = User.query.filter_by(username=user2.username).first()
        assert check_user == user2

    def test_delete_username(self, db):
        user = User.query.first()
        db.session.delete(user)
        db.session.commit()
        delete_user = User.query.filter_by(username=user.username).first()
        assert delete_user is None
