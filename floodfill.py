"""
-------------------------------------------
	Flood Fill Algorithm implementation.
-------------------------------------------
"""
import queue
import random
from PIL import Image, ImageDraw

'''
---------------------------------------------
	Necessary Algorithmic Functions/Classes
---------------------------------------------
'''
class Pair(object):
	x = 0
	y = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
def isSafe(M, m, n, x, y, target):
	if ((x >= 0) and (x < m) and (y >= 0) and (y < n) and (M[x][y] == target)):
		return True
	else:
		return False

def processed(P, x, y):
	ret = False
	
	for i in range(len(P)):
		if (P[i].x == x and P[i].y == y):
			ret = True
	
	return ret
	
def floodFill(M, x, y, replacementColor):
	m = len(M)
	n = len(M[0])
	P = []
	
	# Initialize queue and append the starting pixel (x, y).
	q = queue.Queue()
	pr = Pair(x, y)
	q.put(pr)
	
	# Get target color.
	target = M[x][y]
	
	while not(q.empty()):
		coordPair = q.get()
		coordX = coordPair.x
		coordY = coordPair.y
		
		if (not(processed(P, coordX, coordY))):
			M[coordX][coordY] = replacementColor;
			
			for k in range(len(row)):
				if (isSafe(M, m, n, coordX + row[k], coordY + col[k], target)):
					q.put(Pair(coordX + row[k], coordY + col[k]))
			
			P.append(Pair(coordX, coordY))
				
	return M

	
'''
--------------------------------
	Implementation
--------------------------------
'''
# Define colors dictionary.
colors = {'R': (237, 28, 36), 'G': (34, 177, 76), 'B': (63, 72, 204), 'Y': (255, 242, 0), 'W': (255, 255, 255)}

# Implementation specific functions.
def readImg(imgPath):
	img = Image.open(imgPath)
	pixel_values = [[0 for x in range(img.size[0])] for y in range(img.size[1])]
	
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			pixel_values[i][j] = rgbToPixelChar(img.getpixel((i, j)))
	
	return pixel_values

def rgbToPixelChar(rgbVal):
	pixCh = ''
	
	for key, val in colors.items():
		if (val == rgbVal):
			pixCh = key
			
	return pixCh
	
# Define possible movements.
row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

# Image Processing.
path = "picture.png"
targetXY = (2, 3)
replacement = 'B'

# Read pixel values.
values = readImg(path)

# Do floodfill.
fillValues = floodFill(values, targetXY[0], targetXY[1], replacement)
# print(fillValues)

# Create new image and draw it.
newImg = Image.new('RGB', ((len(fillValues)), len(fillValues[0])))

for i in range(len(fillValues)):
	for j in range(len(fillValues[i])):
		newImg.putpixel((i, j), colors[fillValues[i][j]])
	
newImg.save("processedPic.png")