from geek_space import db
from datetime import datetime
import enum


class StatusNote(enum.Enum):
    CREATED = 'created'
    START = 'start'
    PAUSE = 'pause'
    FINISHED = 'finished'
    PROCESS = 'process'
    ARCHIVED = 'archived'
    DELETED = 'deleted'


class Note(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    start_datetime = db.Column(db.DateTime)
    end_datetime = db.Column(db.DateTime)
    status = db.Column(db.Enum(StatusNote), default=StatusNote.CREATED)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
