"""Day 8 challenge for Advent of Code 2019 - https://adventofcode.com/2019/day/8"""

from os import path
from unittest import TestCase


class ChallengeTests(TestCase):
    """Tests for day 8."""

    def test_part1(self):
        """Test part one example values."""
        test = {
            "width": 3,
            "height": 2,
            "data": "123456789012",
            "result": [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]],
        }
        image = SpaceImage(test["width"], test["height"], test["data"])
        self.assertEqual(image.layers[0].pixels, test["result"][0])
        self.assertEqual(image.layers[1].pixels, test["result"][1])

    def test_part2(self):
        """Test part two example values."""
        test = {
            "width": 2,
            "height": 2,
            "data": "0222112222120000",
            "result": [[0, 1], [1, 0]],
        }
        image = SpaceImage(test["width"], test["height"], test["data"])
        self.assertEqual(image.flattened(), test["result"])


class SpaceImageLayer():
    """Space Image Format Layer."""

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.pixels = []
        for row in range(0, self.height):
            self.pixels.append([])
            for col in range(0, self.width):
                pixel = int(data[row * self.width + col])
                self.pixels[row].append(pixel)

    def count_pixels(self, pixel_value):
        """Returns the number of pixels in this layer matching `pixel_value`."""
        count = 0
        for row in self.pixels:
            for pixel in row:
                if pixel == pixel_value:
                    count += 1
        return count


class SpaceImage():
    """Space Image Format."""

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.layers = []
        self._read_image(data)

    def _read_image(self, data):
        i = 0
        chunk_size = self.width * self.height
        while i < len(data):
            layer = SpaceImageLayer(self.width, self.height, data[i:i + chunk_size])
            self.layers.append(layer)
            i += chunk_size

    def flattened(self):
        """Returns the flattened layer result."""
        result = self.layers[0].pixels.copy()
        for layer in self.layers[1:]:
            for row in range(self.height):
                for col in range(self.width):
                    if result[row][col] == 2:
                        result[row][col] = layer.pixels[row][col]
        return result

    @property
    def layer_with_least_zeroes(self):
        """Returns the `SpaceImageLayer` object with the fewest zero pixels."""
        result = None
        least_zeroes = None
        for layer in self.layers:
            this_count = layer.count_pixels(0)
            if least_zeroes is None or this_count < least_zeroes:
                result = layer
                least_zeroes = this_count
        return result


def run_challenge():
    """Run the challenge."""

    input_file = path.join(path.dirname(__file__), "input.txt")
    with open(input_file, 'r') as data:
        image_data = data.readline()
    image = SpaceImage(25, 6, image_data)
    layer = image.layer_with_least_zeroes
    part_one_solution = layer.count_pixels(1) * layer.count_pixels(2)
    print(f"\tPart one solution: {part_one_solution}")
    part_two_solution = image.flattened()
    print(f"\tPart two solution:\n")
    for row in part_two_solution:
        row_str = ""
        for pixel in row:
            row_str += "|||" if pixel else "   "
        print(f"\t{row_str}")
