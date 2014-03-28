import pylab as pl
import numpy as np
from data import load_responses

songs, responses = load_responses()

fig1 = pl.figure(1)

# Plot mean values
mean_vectors = [(s, np.median(r, axis=0)) for s, r in responses.items()]
track = dict(mean_vectors)['wav/drums-short/wham-drums-2.wav']

plot1 = fig1.add_subplot(121)
plot1.plot(track, 'go')
plot1.ylabel = ('Procent %')
labels = ('Pop', 'Rock', 'Reggae', 'Jazz', 'Klassiskt')
pl.xticks(range(0,5), labels, rotation=20)
pl.ylim([0,100])
pl.xlim([-.5,5])
pl.title('Wham - Mean values')

# Plot boxplot and whiskers
track = responses['wav/drums-short/wham-drums-2.wav']
pop = [r[0] for r in track]
rock = [r[1] for r in track]
reggae = [r[2] for r in track]
jazz = [r[3] for r in track]
classical = [r[4] for r in track]
plot_data = [pop, rock, reggae, jazz, classical]

plot2 = fig1.add_subplot(122)
plot2.boxplot(plot_data)
pl.ylabel = ('Procent %')
labels = ('Pop', 'Rock', 'Reggae', 'Jazz', 'Klassiskt')
pl.xticks(range(1,6), labels, rotation=20)
pl.title('Wham - Boxplot')

# Show
pl.show()
