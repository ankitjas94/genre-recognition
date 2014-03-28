import pylab as pl
import numpy as np
from data import load_responses

songs, responses = load_responses()

# Print table of median values
median_vectors = dict([(s, np.median(r, axis=0)) for s, r in responses.items()])
for s, v in median_vectors.items():
    print "%s\t%s" % (s.split('/')[2].split('.')[0], '\t'.join(str(val) for val in v))

# Plot mean values
fig1 = pl.figure(1)

track = median_vectors['wav/drums-short/wham-drums-2.wav']

plot1 = fig1.add_subplot(121)
plot1.plot(track, 'go')
plot1.ylabel = ('Procent %')
labels = ('Pop', 'Rock', 'Reggae', 'Jazz', 'Klassiskt')
pl.xticks(range(0,5), labels, rotation=20)
pl.ylim([0,100])
pl.xlim([-.5,5])
pl.title('Wham - Medel')

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

# Show plots
pl.show()
