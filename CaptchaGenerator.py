# def printCaptcha():

import string
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
# from matplotlib.tests.test_mathtext import fonts
from numpy import random

if __name__ == '__main__':
	img = np.zeros(shape=(25, 60, 3), dtype=np.uint8)

	img_pil = Image.fromarray(img + 255)
	draw = ImageDraw.Draw(img_pil)

	size = random.randint(10, 16)
	length = random.randint(4, 8)
	img = np.zeros(((size * 2) + 5, length * size, 3), np.uint8)

	# font = random.choice(fonts)
	font = ImageFont.truetype(font='arial', size=12)

	text = "".join(
		random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
		for _ in range(length))

	text = "KRUNAL"

	draw.text((5, 10),
	          text,
	          font=font,
	          fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

	draw.line([(random.choice(range(length * size)), random.choice(range((size * 2) + 5))),
	           (random.choice(range(length * size)), random.choice(range((size * 2) + 5)))],
	          width=1, fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

	thresh = random.randint(1, 5) / 100
	img = cv2.blur(img, (int(size / random.randint(5, 10)), int(size / random.randint(5, 10))))

	cv2.imshow('OpenCV', np.array(img_pil))
	cv2.waitKey()  # Displays the image till a key is pressed
	cv2.destroyAllWindows()
