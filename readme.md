# Threshold and add alpha channel in opencv-python

This simple project takes an image containing a "dark" and "light" area, thresholds it such that the "light" intensity is set to black and the "dark" intensity is set to dark.
Then, it add an alpha channel in order to add max transparency to the white pixels.

It's a useful tool e.g. for obtaining the text portion out of an image.

Feel free to add any contribution and reuse the tool anyway you like.

## Requirements

Install python-opencv (e.g. `pip install opencv-python`).

## Usage

Basic usage:

`threshold.py --img_in <path to input image> --img_out <path to output image>`

Additional arguments:

`--resize_factor`: resizes the image of the desired factor using LANCZOS4 interpolation. (E.g. a factor of 2 doubles the size of the output image, a factor of 0.5 halves it).

`--thresh`: threshold (in grayscale intensity) below which a pixel is considered black and above which it's considered black. Defaults to 100.