from PIL import Image
import numpy as np
from imageReader import *
import unittest
"""
	This class test imageReader
"""

class imageReaderTest(unittest.TestCase):

	# Test read_digit_sequence
	def test_read_axis(self):
		# sample1_reading = read_image("sample1.png")
		# expected_reading_test1 = [2, 1, 0, 1, 1, 1, 0, 2, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 3, 0]
		# self.assertEqual(sample1_reading, expected_reading_test1)
		
		# sample2_reading = read_image("sample2.png")
		# expected_reading_test2 = [2, 30, 7, 6, 33, 13, 4, 6, 8, 6, 11, 3, 13, 7, 4, 8, 10, 7, 9, 2, 9, 4, 7, 3, 6, 7, 1, 2, 1, 1, 7, 5, 2, 4, 2, 10, 8, 5, 4, 8, 3, 10, 7, 7, 7, 12, 7, 10, 6, 6, 2, 2, 4, 6, 10, 21, 6, 6, 14, 57, 22]
		# self.assertEqual(sample2_reading, expected_reading_test2)
		
		# sample3_reading = read_image("sample3.png")
		# expected_reading_test3 = [0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		# self.assertEqual(sample3_reading, expected_reading_test3)

		# sample4_reading = read_image("sample4.tiff")
		# expected_reading_test4 = [49, 199, 136, -22, 32, 42, 56, 2, 0, 0, 0, 10, 5, 0, 0, -27, 0, 10, 10, 0, 0, 0, 0, 100, 361, 172, 10, 10, 162, 123, 70]
		# self.assertEqual(sample4_reading, expected_reading_test4)

		# test1_reading = read_image("test1.png")
		# expected_reading_test1 = [28, 12, 1, 3, 1, 2, 3, 1, 0, 1, 0, 2, -1, 2, 1, 0, 2, 2, 0, 0, 2, 0, 0, 1, -1, -1, 0, -1, 5, 3, 6]
		# self.assertEqual(test1_reading, expected_reading_test1)

		# test2_reading = read_image("test2.png")
		# expected_reading_test2 = [35052, 11083, 3458, 2110, 1097, 867, 679, 6442, 2803, 1305, 844, 632, 491, 869, 1327, 968, 820, 749, 542, 629, 583, 426, 408, 380, 431, 367, 337, 202, 149, 416, 999, 1002]
		# self.assertEqual(test2_reading, expected_reading_test2)

		# test3_reading = read_image("test3.png")
		# expected_reading_test3 = [8, 9, 6, 4, 2, 3, 0, 1, -1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 4, 1, 2]
		# self.assertEqual(test3_reading, expected_reading_test3)

		# test4_reading = read_image("test4.png")
		# expected_reading_test4 = [200, 20, 0, 0, 0, 0, 0, 0, 0, 0, 55, 415, 195, 381, 367]
		# self.assertEqual(test4_reading, expected_reading_test4)

		# test5_reading = read_image("test5.png")
		# expected_reading_test5 = [39079, 5744, 1780, 5508, 1559, 4498, 0, 3478, 5643, 1003, 9905, 5349, 2791, 5952, 1614, 30, 1189, 2386, 5564, 1657, 1687, 1473, 1448, 884, 30, 830, 2, 929, -2157, 522, 100, 1633, 0, 4058, 930, 1993, 34, 5382, 4701, 8822, 11248]
		# self.assertEqual(test5_reading, expected_reading_test5)

		# test6_reading = read_image("test6.png")
		# print(test6_reading)
		# expected_reading_test6 = [39079, 5744, 1780, 5508, 1559, 4498, 0, 3478, 5643, 1003, 9905, 5349, 2791, 5952, 1614, 30, 1189, 2386, 5564, 1657, 1687, 1473, 1448, 884, 30, 830, 2, 929, -2157, 522, 100, 1633, 0, 4058, 930, 1993, 34, 5382, 4701, 8822, 11248]
		# self.assertEqual(test6_reading, expected_reading_test6)

		# test7_reading = read_image("test7.png")
		# expected_reading_test7 = [111, 178, 319, 143, 65, 128, 56, 390, 50, 0, 296, 20, 250, 0, 28, 143, 110, 20, 20, 78, 20, 120, 1698, 250, 0, 60, 161, 0, 0, 0, 196, 50, 115, 148]
		# self.assertEqual(test7_reading, expected_reading_test7)

		# test8_reading = read_image("test8.png")
		# expected_reading_test8 = [0, 240, 75, 25, 0, 395, 220, 20, 0, 0, 100, 0, 0, 155, 0, 0, 270, 250, 100, 0, 0, 0, 0, 0, 0, 45, 0, 50, 500, 0, 50, 100, 350, 10, 1075, 455, 100, 325, 512, 352, 25, 205, 725, 331, 1732]
		# self.assertEqual(test8_reading, expected_reading_test8)

		test9_reading = read_image("test9.png")
		print(test9_reading)
		expected_reading_test8 = 0
		# self.assertEqual(test8_reading, expected_reading_test8)


if __name__ == '__main__':
	unittest.main()

