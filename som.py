import numpy as np
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
units = 100
gridSide = np.sqrt(units)

# randomly assigned weights, one for each property
w = np.random.rand(units, len(properties))
# decreasing list of neighbourhood sizes
nbs = np.arange(2, gridSide, 2)[::-1]

# Calculate weight matrix
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

# calculate the order
order = {}
for x in songs:
    # Locate weight vector with closest distance to input
    diff = prop_dict[x] - w
    dist = np.sum(diff**2, axis=1)
    winner = np.argmin(dist)
    # Assign the winning unit as the index for this animal
    order[x] = winner #toGrid(winner)

print sorted(songs, cmp=compare)