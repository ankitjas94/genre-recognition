import sys
import json
import pylab as pl
import numpy as np
from data import load_responses

songs, responses = load_responses()

# group responses on genre
fo = open('data/mix.genres.json', 'r')
genres = json.loads(fo.read())
cmap = {'pop': 0, 'rock': 1, 'reggae': 2, 'jazz': 3, 'classical': 4}
genre_responses = dict((genres[k], responses[k]) for k in songs)
fo.close()

# Print table of mean values
mean_vectors = dict([(s, np.mean(r, axis=0)) for s, r in genre_responses.items()])
std_dev = dict([(s, np.std(r, axis=0)) for s, r in genre_responses.items()])
print "Mean values:"
for s, v in mean_vectors.items():
    print "%s\t%s" % (s, '\t'.join(str(val) for val in v))
print "Standard deviation:"
for s, v in std_dev.items():
    print "%s\t%s" % (s, '\t'.join(str(val) for val in v))

means = [v[cmap[g]] for g, v in mean_vectors.items()]
std = [v[cmap[g]] for g, v in std_dev.items()]

# Plot mean values with error bars
fig1 = pl.figure(1)

plot1 = fig1.add_subplot(111)
plot1.bar(range(0,5), means, 0.2, color='r', yerr=std)
plot1.ylabel = ('Procent %')
labels = ('Pop', 'Rock', 'Reggae', 'Jazz', 'Klassiskt')
pl.xticks(range(0,5), labels, rotation=20)
pl.ylim([0,100])
pl.xlim([-.5,5])
pl.title('Genreskattningar')

# Show plots
pl.show()
