import os

IMAGE_SIZE = 128                                                                         # image size fixed to 128 px
SCREEN_SIZE = 512                                                                                 # screen size fixed
NUM_TILES_SIDE = 4                                                            # total count of tiles on each side = 4
NUM_TILES_TOTAL = 16                                                                        # total tiles count to 16
MARGIN = 4                                                                                           # margin to 4 px

ASSET_DIR = 'assets'                                                                      # asset_dir named to assets
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']   # load each file in asset_dir folder if
																																														# it has extension of png
assert len(ASSET_FILES) == 8                                                                 # total files stored = 8
