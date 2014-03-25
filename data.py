import json

def load_features(filepath):
    fo = open(filepath, 'r')
    raw_data = json.loads(fo.read())
    songs = raw_data.keys()
    properties = raw_data[songs[0]].keys()
    prop_dict = dict([(s, [float(v) for p, v in d.items()]) for (s, d) in raw_data.items()])
    return (songs, properties, prop_dict)
