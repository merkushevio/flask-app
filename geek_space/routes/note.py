from flask import render_template, abort, redirect, flash, url_for, request
from flask_login import current_user, login_required
from geek_space import app, db
from geek_space.forms.note import NoteForm
from geek_space.models.note import Note


@app.route('/notes')
@login_required
def notes():
    user_notes = Note.query.filter_by(user_id=current_user.id)
    return render_template('note.html', title='Notes', data=user_notes)


@app.route('/note/<int:note_id>')
@login_required
def note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        abort(403)
    return render_template('note.html', title=note.title, note=note)


@app.route('/note/<int:note_id>/update', methods=['GET', 'POST'])
@login_required
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        abort(403)
    form = NoteForm()
    if request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.content
        form.status.data = note.status
        form.created_at.data = note.created_at
        form.start_datetime.data = note.start_datetime
        form.end_datetime.data = note.end_datetime
    if form.validate_on_submit():
        pass
    return render_template('note.html', title='Note')


@app.route('/note/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        abort(403)
    db.session.delete(note)
    db.session.commit()
    flash(f'Your note has been deleted!', 'success')
    return redirect(url_for('notes'))


@app.route('/note/new')
@login_required
def new_note():
    return render_template('note.html', title='Note')
