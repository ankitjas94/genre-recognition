import json
import numpy as np
import pylab as pl
from data import load_features


def toGrid(i):
    return np.array((i % gridSide, i // gridSide))

def fromGrid(i, j):
    return int(i + j * gridSide)

def distance(p1, p2):
    return np.sqrt(sum((p2-p1)**2))

def compare(x, y):
    if order[x] < order[y]:
        return-1
    if order[x] > order[y]:
        return 1
    return 0


# load feature data
songs, properties, prop_dict = load_features('data/features/drums.raw.json')

eta = 0.2
units = 200
gridSide = np.sqrt(units)

# randomly assigned weights, one for each property
w = np.random.rand(units, len(properties))
# decreasing list of neighbourhood sizes
nbs = np.arange(2, gridSide, 2)[::-1]

# calculate weight matrix
for nbh in nbs:
    for x in songs:
        # Locate weight vector with closest distance to input
        diff = prop_dict[x] - w
        dist = np.sum(diff**2, axis=1)
        winner = np.argmin(dist)
        # Find the neighbourhood
        delta = int(np.floor(nbh/2))
        neighbourhood = np.array([toGrid(x) for x in range(units) if distance(toGrid(x), toGrid(winner)) <= delta])
        # Update the weights of all nodes in the neighbourhood
        for p in neighbourhood:
            i = fromGrid(*p)
            w[i] += diff[i] * eta

# calculate the coordinates
order = {}
for x in songs:
    # Locate weight vector with closest distance to input
    diff = prop_dict[x] - w
    dist = np.sum(diff**2, axis=1)
    winner = np.argmin(dist)
    # Assign the winning unit as the index for this animal
    order[x] = toGrid(winner)

# plot results
# get genre data
fo = open('data/drums.genres.json', 'r')
genres = json.loads(fo.read())
colors = [ord(genres[k][0])+ord(genres[k][1]) for k in order.keys()]
fo.close()

pl.rcParams['figure.figsize'] = (12.0, 10.0)
points = np.array(order.values())
labels = np.array([k.split('/')[2].split('-')[0] for k in order.keys()])
pl.scatter(points[:,0], points[:,1], c=colors)

# print labels

for i, (label, x, y) in enumerate(zip(labels, points[:,0], points[:,1])):
    dy = 0.1 if i % 2 else -0.5
    dx = 0.1 if i % 2 else -0.3
    pl.annotate(label, xy=(x+dx, y+dy))
        #textcoords = 'offset points', ha = 'right', va = 'bottom',
        #bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

pl.show()