import os
from PIL import Image


def resize_and_rotate_image(old_path, new_path, grades, size1, size2, format):
    for i in os.listdir(old_path):
        if '.' not in i[0]:
            im = Image.open(old_path + i)
            fn, fext = os.path.splitext(i)
            im.rotate(grades).resize((size1, size2)).convert("RGB").save(new_path + "{}.{}".format(fn, format))
            im.close()




