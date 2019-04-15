from geek_space import app
from geek_space.forms.note import NoteForm
from flask import Response, render_template, request


@app.route('/note', methods=['GET', 'POST'])
def register():
    form = NoteForm()
    return render_template('home.html', title='Notes', form=form)




