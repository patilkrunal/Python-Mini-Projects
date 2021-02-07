#! python3
# stopwatch.py - A simple stopwatch program.

import time


def function():
	# Display the program's instructions.
	print('Press ENTER to begin. Then press ENTER to "click" the stopwatch. '
	      'Press Ctrl - C to quit.')
	input()                     # press Enter to begin
	print('Started.')
	startTime = time.time()     # get the first lap's start time
	lastTime = startTime
	lapNum = 1

	# Start tracking the lap times.
	try:
		while True:
			input()
			lapTime = round(time.time() - lastTime, 2)
			totalTime = round(time.time() - startTime, 2)
			print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
			lapNum += 1
			lastTime = time.time()  # reset the last lap time
	except KeyboardInterrupt:
		# Handle the Ctrl-C exception to keep its error message from displaying.
		print('\nDone.')

if __name__ == '__main__':
	function()


# Prettified Stopwatch: rjust() & ljust() string methods to “prettify” output.
#
# Lap # 1: 3.56 ( 3.56)
# Lap # 2: 8.63 ( 5.07)
# Lap # 3: 17.68 ( 9.05)
# Lap # 4: 19.11 ( 1.43)