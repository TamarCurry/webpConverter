import sys
import os
from PIL import Image

print(str(sys.argv))

if len(sys.argv) <= 1:
    print('No image specified.')
    sys.exit()

imageSrc = sys.argv[1]

isWebp = True;
isWebp = isWebp and os.path.isfile(imageSrc);
isWebp = isWebp and imageSrc[-5:].lower() == ".webp"

if not isWebp:
    print('No webp image at the specified location')
    sys.exit()

print('Converting webp');

with Image.open(imageSrc) as image:
    imageDest = imageSrc[:-5] + ".png"
    image.save( imageDest )