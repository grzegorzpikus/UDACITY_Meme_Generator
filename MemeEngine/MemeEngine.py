"""This script creates a meme is created"""
from PIL import Image
from PIL import ImageDraw, ImageFont
import time
import random
import textwrap
import PIL


class MemeEngine:
    """A class that creates and saves a meme."""

    def __init__(self, output_dir):
        """Save the generated images"""
        self.output_dir = output_dir

    def make_meme(self, path, message, author, width=500):
        """A method that creates a meme form a picture and quotation and its
        author signature.
        """
        try:
            img = Image.open(path)
            width_img = img.width
            height_img = img.height

            if width_img != 500:
                new_height_img = int((width * height_img) / width_img)
                resized_img = img.resize((width, new_height_img))
            else:
                resized_img = img

            draw = ImageDraw.Draw(resized_img)
            font = ImageFont.truetype(font='MemeEngine/LilitaOne-Regular.ttf',
                                      size=30)

            if message is not None:
                message = textwrap.fill(text=message, width=35)
                draw.text((0.02 * resized_img.width, random.uniform(0.05, 0.30)
                           * resized_img.height), message, font=font,
                          fill='white', stroke_width=2, stroke_fill='black')

            if author is not None:
                draw.text((0.6 * resized_img.width, random.uniform(0.7, 0.95)
                           * resized_img.height), author, font=font,
                          fill='white', stroke_width=2, stroke_fill='black')

        except PIL.UnidentifiedImageError:
            img = Image.open('MemeEngine/white.jpg')
            width_img = img.width
            height_img = img.height
            if width_img != 500:
                new_height_img = int((width * height_img) / width_img)
                resized_img = img.resize((width, new_height_img))
            else:
                resized_img = img
            draw = ImageDraw.Draw(resized_img)
            font = ImageFont.truetype(font='MemeEngine/LilitaOne-Regular.ttf',
                                      size=30)
            draw.text((0.18 * resized_img.width, 0.45 * resized_img.height),
                      'Invalid  image  url  entered', font=font, fill='white',
                      stroke_width=2, stroke_fill='black')

        out_path = self.output_dir + "/" + str(time.time()) + '.jpg'
        resized_img.save(out_path)

        return out_path

