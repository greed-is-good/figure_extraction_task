import numpy

is_debug_on = False
error_return = -100000
dollar_sign_return_value = -2
negative_sign_return_value = -3
comma_return_value = -4
pound_return_value = -5
euro_sign_return_value = -6
letter_k_return_value = -7
letter_r_return_value = -8
def read_digit_sequence(arr):
	'''This function reads a list of single digit

	The function scans the pixels column by column to partition digits. Each single digit starts
	with a column containing black pixel and ends with a column containing no black pixel. Then the
	function reads each digit to return the digit represented.

	Args:
	arr (int): The 2D numpy array to represent the pixel values.

	Returns:
	int: The digit represented by the pixel
	error_return for error.
	'''

	if is_debug_on :
		print("\nread_digit_sequence with param:\n")
		print("size of param:", arr.shape)
		for x in range(arr.shape[0]):
			print(arr[x])

	# Each digit read from the pixels
	result = []

	# First scan the pixel columns to distinguish each digit from each other
	# Each digit should be separated by a non black column
	# The column been scanned right now
	current_column = 0

	# Starting and ending column of a digit, reset to -1 after find a digit
	starting_column = -1
	ending_column = -1

	# Used to mark the - sign read
	is_negative = False

	while(current_column < arr.shape[1]) :
		while(starting_column == -1 and current_column < arr.shape[1]) :
			has_black_pixel = False
			for i in range(arr.shape[0]):
				if (arr[i][current_column] == 1):
					has_black_pixel = True
					break

			if has_black_pixel :
				starting_column = current_column

			current_column += 1

		if is_debug_on :
			print("starting_column is ", starting_column)

		# no more digit
		if (starting_column == -1):
			break

		while(ending_column == -1 and current_column < arr.shape[1]) :
			has_no_black_pixel = True
			for i in range(arr.shape[0]):
				if (arr[i][current_column] == 1):
					has_no_black_pixel = False
					break

			if has_no_black_pixel :
				ending_column = current_column

			current_column += 1

		# The last digit in the sequence
		if (ending_column == -1):
			ending_column = arr.shape[1] - 1

		if is_debug_on :
			print("ending_column is ", ending_column)

		temp = numpy.zeros((arr.shape[0], ending_column - starting_column + 1))

		for x in range(temp.shape[0]):
			for y in range(temp.shape[1]):
				temp[x][y] = arr[x][starting_column + y]

		try:
			digit = pixel_array_to_digit(temp)
		except IndexError:
			if is_debug_on:
				print("index of out bound error")
			digit = error_return

		if (digit == error_return) :
			return error_return

		if (digit == negative_sign_return_value):
			is_negative = True
		else:
			if (digit != comma_return_value):
				result.append(digit)

		# search for next digit
		starting_column = -1
		ending_column = -1

	if (len(result) == 0):
		if is_debug_on:
			print("Error: no digit is read")
		return error_return

	final_result = 0

	if is_debug_on :
		print("read_digit_sequence: adding up final result, count ", len(result))

	for x in range(len(result)):
		if is_debug_on :
			print("adding : ", result[x] * (10 ** (len(result) - x - 1)))
		final_result += result[x] * (10 ** (len(result) - x - 1))

	if (is_negative):
		final_result *= -1

	return final_result

def verify_digit_pixels(arr, digit, left_most_x, left_most_y):
	'''This function verifies whether the digit returned by pixel_array_to_digit is correct.

	The function checks all expected black pixels to verify the reading.If the digit
	read is wrong, return error_return

	Args:
	arr(int):The 2D numpy array to represent the pixel values.
	arr[row][column] is the pixel values at that row and column
	digit(int): digit read by pixel pixel_array_to_digit
	left_most_x: row number of left upper most black pixel
	left_most_x: column number of left upper most black pixel

	Returns:
	int: digit if read correctly, else return error_return
	'''

	if is_debug_on:
		print("verify_digit_pixels is called with param (arr, digit, left_most_x, left_most_y)")
		print(arr, digit, left_most_x, left_most_y)

	if(digit == 1):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1):
			return 1

	if(digit == 2):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1
		   and arr[left_most_x + 4][left_most_y + 3] == 1):
			return 2

	if(digit == 3):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1):
			return 3

	if(digit == 4):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y + 3] == 1):
			return 4

	if(digit == 5):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1):
			return 5

	if(digit == 6):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 6

	if(digit == 7):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 4][left_most_y + 1] == 1):
			return 7

	if(digit == 8):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 8

	if(digit == 9):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 9

	if(digit == 0):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1):
			return 0

	# dollar_sign_return_value for $
	if(digit == dollar_sign_return_value):
		if(arr[left_most_x - 2][left_most_y + 2] == 1
		   and arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x - 1][left_most_y + 3] == 1
		   and arr[left_most_x - 1][left_most_y + 4] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y + 4] == 1
		   and arr[left_most_x + 3][left_most_y] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y + 2] == 1):
			return 0

	# pound_return_value for pound sign
	if(digit == pound_return_value):
		if(arr[left_most_x - 2][left_most_y + 2] == 1
		   and arr[left_most_x - 2][left_most_y + 3] == 1
		   and arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y ] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y + 3] == 1):
			return 0

	# pound_return_value for euro sign
	if (digit == euro_sign_return_value):
		if(arr[left_most_x - 1][left_most_y + 1] == 1
		   and arr[left_most_x - 1][left_most_y + 2] == 1
		   and arr[left_most_x - 1][left_most_y + 3] == 1
		   and arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 1] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 3][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1):
			return 0

	# letter_k_return_value for k letter in krone
	if (digit == letter_k_return_value):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 3] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 2] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 3][left_most_y] == 1
		   and arr[left_most_x + 3][left_most_y + 2] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 3] == 1):
			return 0

	# letter_r_return_value for r letter in krone
	if(digit == letter_r_return_value):
		if(arr[left_most_x][left_most_y] == 1
		   and arr[left_most_x][left_most_y + 1] == 1
		   and arr[left_most_x][left_most_y + 2] == 1
		   and arr[left_most_x + 1][left_most_y] == 1
		   and arr[left_most_x + 1][left_most_y + 3] == 1
		   and arr[left_most_x + 2][left_most_y] == 1
		   and arr[left_most_x + 2][left_most_y + 1] == 1
		   and arr[left_most_x + 2][left_most_y + 2] == 1
		   and arr[left_most_x + 3][left_most_y] == 1
		   and arr[left_most_x + 3][left_most_y + 3] == 1
		   and arr[left_most_x + 4][left_most_y] == 1
		   and arr[left_most_x + 4][left_most_y + 3] == 1):
			return 0

	return error_return

def pixel_array_to_digit(arr):
	'''This function converts pixel array into corresponding digits

	The input is 2d binary array with 1 indicating black pixel and 0 indicating
	background pixel. The function first identifies the left most pixel(using the
	upper pixel if tied). Then the function compares the relative position of black
	pixels to determine the digit the pixels is representing. If the function cannot
	determine the digit, error_return will be returned to indicate error.

	Args:
	arr (int): The 2D numpy array to represent the pixel values.
	arr[row][column] is the pixel values at that row and column
	Returns:
	int: The digit read from the pixels.
		error_return if the digit cannot be determined.
		0 if the digit is $.(for computational convenience)
		negative_sign_return_value for - sign

	Throws:
		IndexError

	'''

	# todo: checking for - sign and .

	if is_debug_on:
		print("pixel_array_to_digit is called with param (arr)")
		for x in range (arr.shape[0]):
			print(arr[x])

	# Locate the left upper most black pixel (upper bit on the left most column)
	left_most_x = -1;
	left_most_y = -1;

	# Traverse the array to find the left upper most pixel
	for y in range(arr.shape[1]):
		for x in range(arr.shape[0]):
			if(arr[x][y] == 1):
				left_most_x = x
				left_most_y = y

			if left_most_x != -1:
				break

		if left_most_y != -1:
			break

	if (left_most_x == -1 or left_most_y == -1):
		if is_debug_on:
			print("pixel_array_to_digit cannot find black pixel with arr")
			print(arr)
		return error_return

	if is_debug_on:
		print("left_most_x, left_most_y", left_most_x, left_most_y)

	# Test for - sign
	# TODO: think of a better way to place the code
	if(arr.shape[1] - left_most_y > 2
	   and arr[left_most_x][left_most_y + 1] == 1
	   and arr[left_most_x][left_most_y + 2] == 1):
		if (arr.shape[0] - left_most_x < 2
		    or arr[left_most_x + 2][left_most_y + 2] == 0):
			return negative_sign_return_value

	if is_debug_on:
		print("not - sign")

	# Test for "," mark
	if(left_most_x > 0
	   and arr[left_most_x - 1][left_most_y + 1] == 1):
		if(arr.shape[1] - left_most_y < 3
		   or (arr[left_most_x - 1][left_most_y + 2] == 0
		       and arr[left_most_x][left_most_y + 1] == 0
		       and arr[left_most_x][left_most_y + 2] == 0)):
			return comma_return_value

	if is_debug_on:
		print("not , mark")

	# Test for .0 , the special case of 0 where one black pixel preceeds the 0 on the left
	if (left_most_x > 3 and arr.shape[1] - left_most_y > 5
	    	and arr[left_most_x - 4][left_most_y + 2] == 1
		    and arr[left_most_x - 4][left_most_y + 3] == 1
		    and arr[left_most_x - 3][left_most_y + 1] == 1
		    and arr[left_most_x - 3][left_most_y + 4] == 1
		    and arr[left_most_x - 2][left_most_y + 1] == 1
		    and arr[left_most_x - 2][left_most_y + 4] == 1
		    and arr[left_most_x - 1][left_most_y + 1] == 1
		    and arr[left_most_x - 1][left_most_y + 4] == 1
		    and arr[left_most_x][left_most_y + 2] == 1
		    and arr[left_most_x][left_most_y + 3] == 1):
		#print("here")
		return 0

	if is_debug_on:
		print("not .0 case")


	# A valid digit or $ pixel has at least 5 rows, 2 coloums
	# Quite test for wrong orientation
	if (arr.shape[1] - left_most_y < 2 or arr.shape[0] - left_most_x < 4) :
		# print("pixel_array_to_digit with param ", arr, ": invalid input dimensions")
		return error_return

	# Use a decision tree to decide on the digit represented
	# A flow chart is available on https://github.com/greed-is-good/figure_extraction_task

	if (arr[left_most_x][left_most_y + 1] == 0):
		# {0,4,6,8,9,$,euro,k}
		if (arr[left_most_x + 1][left_most_y] == 0):
			# {8,9,$}
			if (arr[left_most_x + 2][left_most_y] == 1):
				return verify_digit_pixels(arr, 8, left_most_x, left_most_y)
			else :
				# {9,$}
				if (arr[left_most_x][left_most_y + 2] == 0):
					return verify_digit_pixels(arr, 9, left_most_x, left_most_y)
				else :
					# 0 for $
					return verify_digit_pixels(arr, dollar_sign_return_value, left_most_x, left_most_y)

		else :
			# {0,4,6,euro,k}
			if (arr[left_most_x][left_most_y + 3] == 0):
				# {6, euro}
				if (arr[left_most_x - 1][left_most_y + 3] == 0):
					return verify_digit_pixels(arr, 6, left_most_x, left_most_y)
				else :
					return verify_digit_pixels(arr, euro_sign_return_value, left_most_x, left_most_y)
			else :
				# {0,4,k}
				if(arr[left_most_x + 2][left_most_y + 1] == 0):
					return verify_digit_pixels(arr, 0, left_most_x, left_most_y)
				else :
					# {4, K}
					if (arr[left_most_x + 3][left_most_y] == 0):
						return verify_digit_pixels(arr, 4, left_most_x, left_most_y)
					else :
						return verify_digit_pixels(arr, letter_k_return_value, left_most_x, left_most_y)

	else :
		# {1,2,3,5,7,pound,R}
		if (left_most_x > 0 and arr[left_most_x - 1][left_most_y + 1] == 1):
			return verify_digit_pixels(arr, pound_return_value, left_most_x, left_most_y)

		if (arr[left_most_x + 4][left_most_y] == 0):
			# {1,7}
			if (arr[left_most_x + 1][left_most_y + 1] == 0):
				return verify_digit_pixels(arr, 7, left_most_x, left_most_y)
			else :
				return verify_digit_pixels(arr, 1, left_most_x, left_most_y)

		else:
			# {2,3,5,R}
			if (arr[left_most_x + 1][left_most_y] == 0):
				# {2,3}
				if (arr[left_most_x + 3][left_most_y] == 0):
					return verify_digit_pixels(arr, 3, left_most_x, left_most_y)
				else :
					return verify_digit_pixels(arr, 2, left_most_x, left_most_y)

			else:
				# {5,R}
				if (arr[left_most_x + 3][left_most_y] == 0):
					return verify_digit_pixels(arr, 5, left_most_x, left_most_y)
				else :
					return verify_digit_pixels(arr, letter_r_return_value, left_most_x, left_most_y)
