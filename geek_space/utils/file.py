import secrets
import os
from geek_space import app
from PIL import Image


def save_picture(form_image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = f'{random_hex}{f_ext}'
    picture_path = os.path.join(app.root_path, 'static/img/profile_pics', image_fn)

    output_size = (125, 125)
    i = Image.open(form_image)
    i.thumbnail(output_size)
    i.save(picture_path)

    return image_fn
