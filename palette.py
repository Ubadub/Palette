from PIL import Image
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import math
import colorsys

PALETTE_WIDTH = 800
PALETTE_HEIGHT = 200
MAX_SIZE = 500,500

def make_palette(file):
	"""
	Given the path of a file, returns a list of 8 lists, each of which describes
	an RGB color as [R, G, B].
	"""
	im = Image.open(file)

	# first, resize image so that the clustering doesn't take forever.
	im.thumbnail(MAX_SIZE)

	pixels = np.array([im.getpixel((x,y)) for x in range(0, im.size[0]) for y in range(0, im.size[1])])
	clt = MiniBatchKMeans() # default is 8 clusters
	clt.fit(pixels)
	return [[int(round(i)) for i in color] for color in clt.cluster_centers_]

def perceived_brightness (r, g, b):
	"""
	Calculates perceived brightness for the given RGB values.

	Thank you to Darel Rex Finley (http://alienryderflex.com/hsp.html)
	for devising this formula.
	"""
	return math.sqrt((.299 * r * r) + (.587 * g * g) + (.114 * b * b))

def hsp_rank (r, g, b, mult=8):
	"""
	Combines hue, saturation, and perceived brightness info for a
	smoother sort. In order to dampen the impact of the way Python
	sorts tuples (by comparing each element in order), we multiply each
	of the elements of the tuple to be returned by a constant.
	"""
	lum = perceived_brightness(r, g, b)
	h, s, v = colorsys.rgb_to_hsv(r, g, b)

	return (h * mult, lum * mult, s * mult)

def main():
	cluster_centers = make_palette(input("Enter name of file: "))
	print(cluster_centers)
	cluster_centers.sort(key=lambda rgb: hsp_rank(*rgb))

	pixels = []
	for i in range(8):
		color = tuple(cluster_centers[i])
		print("Color #{}: {}".format(i+1, color))
		for j in range(PALETTE_WIDTH//8 * PALETTE_HEIGHT):
			pixels.append(color)

	img = Image.new('RGB',(PALETTE_HEIGHT,PALETTE_WIDTH))
	img.putdata(pixels) 
	img.show()

if __name__ == '__main__':
	main()