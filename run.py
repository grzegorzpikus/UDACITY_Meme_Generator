import os
import glob
import random
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine.MemeEngine import MemeEngine
from PIL import Image

x = Ingestor.parse('_data/DogQuotes/DogQuotesTXT.txt')
body = x[0].body
author = x[0].author


path = '_data/photos/dog/xander_3.jpg'
image = Image.open(path)





MemeEngine.make_meme(path, body, author)