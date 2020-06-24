import os
import random
import game_config as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)          # store animal file add in animal_count dictionary which
																											# stores count of the animals as well. Initialize count to 0 first
# print(animals_count)

def available_animals():
	l = [a for a, c in animals_count.items() if c < 2]     # load img path of the image in a if count of that animal < 2
	# print(l)
	return l


class Animal:
	def __init__(self, index):
		self.index = index                                                    # load index via argument to class object
		self.row = index //gc.NUM_TILES_SIDE                          # calculate row via index // num_side pixel number
		self.col = index % gc.NUM_TILES_SIDE
		self.name = random.choice(available_animals())                           # randomly give img path to animal name
		animals_count[self.name] += 1                         # animal count incremented whenever animal object is loaded
		
		self.image_path = os.path.join(gc.ASSET_DIR, self.name)                       # create img path via join function
		self.image = image.load(self.image_path)                        # load img via its path in image objects variable
		self.image = transform.scale(self.image, (gc.IMAGE_SIZE-2*gc.MARGIN, gc.IMAGE_SIZE-2*gc.MARGIN))      # set width
																																			# height of the image via transform scale method
		self.box = self.image.copy()                         # create box as same as image. Now its a copy of image itself
		self.box.fill((200, 200, 200))                              # fill the image copy box with grey color (200,200,200)
		self.skip = False                                             # that particular image is in active. Its not skipped
