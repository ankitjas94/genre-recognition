import json
import numpy as np
import pylab as pl
from sklearn import neighbors
from data import load_features, load_mfccs


# Load and divide data

##songs, prop_dict = load_mfccs()
songs, prop_dict = load_features()
training_set = dict([e for e in prop_dict.items()[0:30]])
testing_set = dict([e for e in prop_dict.items()[30:]])


# Train k-NN

fo = open('data/drums.genres.json', 'r')
genres = json.loads(fo.read())
cmap = {'pop': 0, 'rock': 1, 'reggae': 2, 'jazz': 3, 'classical': 4}
classes = [cmap[genres[k]] for k in training_set.keys()]
fo.close()

X = np.array([p for k, p in training_set.items()])
Y = np.array(classes)
n_neighbors = 10
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance').fit(X, Y)


# Test k-NN

validate = np.array([p for k, p in testing_set.items()])

hits = 0.0
misses = 0.0
for s, p in [(s, p) for (s, p) in testing_set.items()]:
    s_name = s.split('/')[2].split('.')[0]
    prediction = clf.predict(prop_dict[s])
    answer = cmap[genres[s]]
    if answer == prediction:
        hits += 1
    else:
        misses += 1
    print s_name, ': ', answer, prediction, answer == prediction

print 'Success rate: ', hits/(hits+misses)
