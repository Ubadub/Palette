from PIL import Image
from sklearn.cluster import MiniBatchKMeans
import numpy as np

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

def main():
	cluster_centers = make_palette(input("Enter name of file: "))

	pixels = []
	for i in range(8):
		for j in range(PALETTE_WIDTH//8 * PALETTE_HEIGHT):
			pixels.append(tuple(cluster_centers[i]))

	img = Image.new('RGB',(PALETTE_HEIGHT,PALETTE_WIDTH))
	img.putdata(pixels) 
	img.show()

if __name__ == '__main__':
	main()