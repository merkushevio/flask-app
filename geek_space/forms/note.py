from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=4, max=100)])
    content = StringField('Content')
    start_datetime = DateTimeField('Start Datetime', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), unique=True, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow)
#     content = db.Column(db.Text)
#     start_datetime = db.Column(db.DateTime)
#     end_datetime = db.Column(db.DateTime)
#     status = db.Column(db.Enum(StatusNote), default=StatusNote.CREATED)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     group = db.Column(db.String, db.ForeignKey('group_note.id'))