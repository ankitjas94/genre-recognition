import json

def load_features(filepath):
    fo = open(filepath, 'r')
    return json.loads(fo.read())
