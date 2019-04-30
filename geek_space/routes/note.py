from flask import render_template, abort, redirect, flash, url_for, request
from flask_login import current_user, login_required
from geek_space import app, db
from geek_space.forms.note import NoteForm
from geek_space.models.note import Note


@app.route('/notes')
@login_required
def notes():
    user_notes = Note.query.filter_by(user_id=current_user.id)
    return render_template('notes/notes.html', title='Notes', notes=user_notes)


@app.route('/note/<int:note_id>')
@login_required
def note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        abort(403)
    return render_template('notes/note.html', title=note.title, note=note, image_file=current_user.image_file)


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
        note.title = form.title.data
        note.content = form.content.data
    return render_template('notes/note.html', title='Note')


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


@app.route('/note/new', methods=['GET', 'POST'])
@login_required
def new_note():
    form = NoteForm()
    image_file = url_for('static', filename=f'img/profile_pics/{current_user.image_file}')
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user = current_user
        group = form.group.data
        note = Note(title=title, content=content, user_id=user.id, group=group)
        db.session.add(note)
        db.session.commit()
        flash(f'Your note is been created!', 'success')
        return redirect(url_for('notes'))
    return render_template('notes/note.html', title='Note', form=form, image_file=image_file)
