from geek_space import db
import enum


class Roles(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Enum(Roles), default=Roles.USER, nullable=False)
    is_enable = db.Column(db.Boolean, default=True)
    image_file = db.Column(db.String(20), default='default.jpg')
    notes = db.relationship('Note', backref='user', lazy=True)

    def __repr__(self) -> str:
        return f'User({self.username}, {self.email}, {self.role}, {self.is_enable}, {self.image_file} )'

