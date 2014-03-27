import json
import numpy as np
import pylab as pl
from data import load_features, load_mfccs


def toGrid(i):
    return np.array((i % gridSide, i // gridSide))

def fromGrid(i, j):
    return int(i + j * gridSide)

def distance(p1, p2):
    return np.sqrt(sum((p2-p1)**2))

# load feature data
#songs, prop_dict = load_features()
songs, prop_dict = load_mfccs()

eta = 0.2
units = 300
gridSide = np.sqrt(units)

# randomly assigned weights, one for each property
w = np.random.rand(units, len(prop_dict.items()[0][1]))
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
fo = open('data/drums.genres.json', 'r')
genres = json.loads(fo.read())
cmap = {'pop': 0, 'rock': 60, 'reggae': 125, 'jazz': 190, 'classical': 255}
colors = [cmap[genres[k]] for k in order.keys()]
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

pl.show()
