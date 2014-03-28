import json
import numpy as np
import pylab as pl
from sklearn import svm
from data import load_features


songs, prop_dict = load_features()

fo = open('data/drums.genres.json', 'r')
genres = json.loads(fo.read())
cmap = {'pop': 0, 'rock': 1, 'reggae': 2, 'jazz': 3, 'classical': 4}
classes = [cmap[genres[k]] for k in prop_dict.keys()  if '-2' not in k]
fo.close()

X = [p for k, p in prop_dict.items() if '-2' not in k]
Y = classes
clf = svm.SVC()
clf.fit(X, Y)

print clf.predict(prop_dict['wav/drums-short/abba-drums-2.wav'])

