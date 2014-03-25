import json
import numpy as np

def load_features(filepath):
    fo = open(filepath, 'r')
    raw_data = json.loads(fo.read())
    # extract data from json dict
    songs = raw_data.keys()
    properties = raw_data[songs[0]].keys()
    props = [[float(v) for p, v in d.items()] for (s, d) in raw_data.items()]
    # scale song properties to 0-1 interval
    mins = np.min(props, axis=0)
    maxs = np.max(props, axis=0)
    rng = maxs - mins
    props = 1 - (maxs - props) / rng
    return (songs, properties, dict(zip(songs, props)))
