import sys
import os.path
from PIL import Image, ImageOps
import PIL

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

file1 = os.path.splitext(sys.argv[1])
file2 = os.path.splitext(sys.argv[2])
extensions = [".jpeg",".jpg",".png"]

if file1[1].lower() not in extensions:
    sys.exit("Invalid input")
elif file2[1].lower() not in extensions:
    sys.exit("Invalid ouput")
elif file1[1].lower() != file2[1].lower():
    sys.exit("Input and output have different extensions")

img = Image.open(sys.argv[1])

transp = Image.open("shirt.png")
size = transp.size

puppet = ImageOps.fit(img, size)
puppet.paste(transp, transp)
puppet.save(sys.argv[2])



