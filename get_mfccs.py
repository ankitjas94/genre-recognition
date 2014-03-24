#!/usr/bin/python
"""get_mfccs.py
Extract raw MFCCs from a list of WAV files. Dumps data in JSON format.

Usage: $ python get_mfccs.py audiofile_1.wav audiofile_2.wav ... audiofile_n.wav
Use --help or -h to see this message.
"""

import sys
import getopt
import json
import scipy.io.wavfile as wav
from features import mfcc

def extract(audiofile):
    (rate,sig) = wav.read(audiofile)
    return (audiofile, mfcc(sig,rate).tolist())

def get_mfccs(files):
    features = dict(map(extract, files))
    print json.dumps(features)
    return 0


# Boilerplate code below

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    """Handle command line arguments"""
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                return 0
        return get_mfccs(args)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
