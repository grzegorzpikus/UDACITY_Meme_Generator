from PIL import Image
from PIL import ImageDraw, ImageFont


class MemeEngine:
    """A class that creates a meme"""

    @classmethod
    def make_meme(cls, path, message, author, width=500):
        """A method that creates a meme form a picture and quotation and its
        author signature"""
        img = Image.open(path)
        width_img = img.width
        height_img = img.height

        if width_img != 500:
            new_height_img = int((width * height_img) / width_img)
            resized_img = img.resize((width, new_height_img))
        else:
            resized_img = img

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font='MemeEngine/LilitaOne-Regular.ttf',
                                  size=40)
        if message is not None:
            draw.text((10, 30), message, font=font, fill='black')

        if author is not None:
            draw.text((300, 400), author, font=font, fill='black')

        split_path = path.split('/')
        out_path = '_data/photos/meme' + '/r_' + split_path[3] + '.jpg'
        resized_img.save(out_path)

        return out_path

