import pygame
import game_config as gc                                                                      # load game_config as gc

from pygame import display, event, image                   # import methods display event and image from pygame module
from animal import Animal                                                      # load Animal class from animal.py file
from time import sleep


def find_index(x, y):                                              # find which index is clicked by maths calculation
	row = y // gc.IMAGE_SIZE                                                     # x//gc.IMAGE_SIZE  == eg. 423//128==3
	col = x // gc.IMAGE_SIZE
	index = row * gc.NUM_TILES_SIDE + col
	return index


def game():
	# pass
	matched = image.load('assets/matched.png')                                    #load image in matched variable
	# print(matched)
	running = True                                                                   # game running variableset to true
	tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]                         # load animal tiles in tiles list
	# print(tiles)
	current_images = []                                                           # define current_images list to empty

	while running:                                                           # while the game is running load the event
		current_events = event.get()

		for e in current_events:
			if e.type == pygame.QUIT:                                       # if event type is game QUIT make running false
				running = False

			if e.type == pygame.KEYDOWN:                                                    # if event type is any keypress
				if e.key == pygame.K_ESCAPE:                             # if event keypress is escape key make running false
					running = False

			if e.type == pygame.MOUSEBUTTONDOWN:                                            # if event type is mouseclicked
				mouse_x, mouse_y = pygame.mouse.get_pos()                                     # get position of mouse clicked
				# print(mouse_x, mouse_y)
				index = find_index(mouse_x, mouse_y)                       # find which index is clicked by maths calculation
				# print(index)
				if index not in current_images:
					current_images.append(index)                    # append recently clicked two indexes to current_image list
				# print(current_images)
				if len(current_images) > 2:                                               # store the recent two indexes only
					current_images = current_images[1:] # whenever current_images length goes above 2 increase 2 that time itself
			# print(current_images)

		screen.fill((255, 255, 255))

		total_skipped = 0

		for _, tile in enumerate(tiles):      # iterate over tiles and store img in image_i if available in current_images
																																																# else store tile.box
			image_i = tile.image if tile.index in current_images else tile.box                  # if tile index available in
																																				# current_image else store tile.box in image_i
			# image_i = tile.image

			if not tile.skip:
				screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
			else:
				total_skipped += 1

		display.flip()                                            # update the game screen after making all above changes

		if len(current_images) == 2:
			idx1, idx2 = current_images
			# print(idx1, idx2)
			if tiles[idx1].name == tiles[idx2].name:                                                  # check if they match
				# pass
				tiles[idx1].skip = True                                                     # remove both them by skip method
				tiles[idx2].skip = True
				sleep(0.4)
				screen.blit(matched, (0, 0))                                            # load matched variable img on screen
				display.flip()                                                                                # upadte screen
				sleep(0.4)
				current_images = []

			if total_skipped == len(tiles):                                                  # if all the tiles are skipped
				running = False


if __name__ == '__main__':
	pygame.init()

	display.set_caption('HIDDEN TILES GAME')
	screen = display.set_mode((512, 512))

	game()

	print("GoodBye!!!")
