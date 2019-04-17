from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from geek_space import app, db
from geek_space.forms.profile import ProfileForm
from geek_space.utils.file import save_picture


@login_required
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    image_file = url_for('static', filename=f'img/profile_pics/{current_user.image_file}')
    form = ProfileForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = save_picture(form.image.data)
            current_user.image_file = image_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your account has been updated', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)

