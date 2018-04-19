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
		
		M[coordX][coordY] = replacementColor;
		
		for k in range(len(row)):
			if (isSafe(M, m, n, coordX + row[k], coordY + col[k], target)):
				q.put(Pair(coordX + row[k], coordY + col[k]))
				
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
targetXY = (8, 10)
replacement = 'B'

values = readImg(path)
fillValues = floodFill(values, targetXY[0], targetXY[1], replacement)

print(fillValues)

'''
# Define colors: Red, Green, Blue, White, Black
colors = ['R', 'G', 'B', 'W', 'X']

# Define your picture size and the picture color matrix.
picH = 10
picW = 10

pic = [['W' for x in range(picH)] for y in range(picW)]

for i in range(picH):
	for j in range(picW):
		pic[i][j] = random.choice(colors)
		
# Print picture color matrix.
print("---------------------")
print("Unfilled picture")
print("---------------------")
for i in range(len(pic)):
	print(pic[i])
	
# Process picture (W -> X at 3, 5)
picF = floodFill(pic, 3, 5, 'X')
print("*** Processing picture at 3, 5. Filling with X ***")

# Print processed picture.
print("---------------------")
print("Filled picture")
print("---------------------")
for i in range(len(picF)):
	print(picF[i])
'''