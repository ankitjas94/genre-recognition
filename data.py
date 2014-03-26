import json
import numpy as np

selected_features = (
    # difference in strength between harmonic and percussive part of audio
    'rms_diff', 'rms_diffLOG', 'rms_diffABSLOG',
    # how "percussive" the song is
    'perc_sal', 'perc_sal2' 'perc_sal3', 'perc_sal4', 'percussion',
    # centroid of the spectrum
    'orgCtrd1',
    # spectrum in bands
    'orgSp3', 'orgSp3db', 'orgSp4', 'orgSp4db',
    # audio strength in octaves
    'orgSpBinOct1', 'orgSpBandOct1', 'orgSpBinOct2', 'orgSpBandOct2', 'orgSpBinOct3', 'orgSpBandOct3', 'orgSpBinOct4', 'orgSpBandOct4', 'orgSpBinOct5', 'orgSpBandOct5', 'orgSpBinOct6', 'orgSpBandOct6', 'orgSpBinOct7', 'orgSpBandOct7', 'orgSp3b', 'orgSp3dbb', 'orgSp4b', 'orgSp4dbb',
    # "harmonic" onsets, different measurements
    'h_on_han1', 'h_on_han1s', 'h_on_han2', 'h_on_han2s', 'h_on_80', 'h_on_80SC', 'h_on_80SCm', 'h_on_80SCl', 'h_on_80FX', 'h_on_100', 'h_on_100SC', 'h_on_100SCm', 'h_on_100SCl', 'h_on_100FX', 'h_on_p10', 'h_on_p10SC', 'h_on_p10SCm', 'h_on_p10SCl', 'h_on_p10FX', 'h_on_p20', 'h_on_p20SC', 'h_on_p20SCm', 'h_on_p20SCl', 'h_on_p20FX',
    # spectral flux for harmonic part
    'harm_flux', 'harm_fluxT', 'harmonic',
    # onsets per second
    'on_sec', 'on_sec_flux', 'sec_on',
    # percussive onsets per second
    'perc_on_sec', 'perc_on_sec_flux', 'perc_sec_on', 'harm_on_sec', 'harm_on_sec_flux', 'harm_sec_on',
    # comparisons between harmonic and percussive parts of db audio level
    'rms_org', 'rms_org10', 'rms_orgLOG', 'rms_org10LOG', 'rms_perc', 'rms_perc10', 'rms_percLOG', 'rms_perc10LOG', 'rms_harm', 'rms_harm10', 'rms_harmLOG', 'rms_harm10LOG', 'rms_percCQT', 'rms_percCQT10', 'rms_percCQTLOG', 'rms_percCQT10LOG', 'rms_harmCQT', 'rms_harmCQT10', 'rms_harmCQTLOG', 'rms_harmCQT10LOG', 'rms_diff10', 'rms_org_vs_harm', 'rms_orgLOGtime', 'rms_percLOGtime', 'rms_harmLOGtime', 'rms_percCQTLOGtime', 'rms_harmCQTLOGtime',
    # weight of onsets regarding distance between them. comparing onsets in the "perceptual now"
    'rel_w', 'rel_w_ctrd', 'rel_w_compare', 'rel_w_compare12', 'rel_w_compare15', 'rel_w_compare2', 'rel_w_compare10', 'rel_wperc', 'rel_w_ctrdperc', 'rel_w_compareperc', 'rel_w_compare12perc', 'rel_w_compare15perc', 'rel_w_compare2perc', 'rel_w_compare10perc',
    # rythmic complexity
    'r_comp1', 'r_comp2', 'r_comp3', 'r_comp4', 'sec_on_str2', 'rel_time', 'pos05', 'pos06', 'pos07', 'pos08', 'posW',
    # different measurements where IOI between clustered drumparts are measured
    ##'clust2speed_han1', 'clust2speed_han2', 'clust2speed_han3', 'clust2speed_han4', 'clust2speed_han5', 'clust2speed_han6', 'clust2speed_s1', 'clust2speed_s2', 'clust2speed_s3', 'StrongCluster_IOI_y', 'clust2speed_s4', 'clust2speed_s5', 'clust2speed_s6', 'clust2speed_s7', 'clust2speed_s8', 'cluster_pass045', 'cluster_pass05', 'StrongCluster_IOI_x', 'cluster_pass055', 'cluster2speed_nofilt', 'cluster2speed_nofilt2', 'cluster2speed_nofilt3', 'cluster2speed_nofilt4', 'cluster2speed_nofilt5', 'cluster2speed_nofilt6', 'clusterW', 'cluster_pass03w', 'cluster_pass05w', 'cluster_pass07w', 'cluster2speed', 'cluster2speed35_41', 'cluster2speed26_50', 'cluster2speed18_70', 'cluster2speedLOG', 'cluster2speed35_41LOG', 'cluster2speed26_50LOG', 'cluster2speed18_70LOG',
    # cepstrum of the next fields histogram
    'cep_period',
    # length of the most significant period in the drums
    'ioi_p',
    # probability of different metres
    'prob24', 'prob44', 'prob34', 'prob68', 'prob1', 'firstpeak100', 'firstpeak90', 'firstpeak80',
    # probability of triple metre
    'raise3',
)

def load_features(filepath):
    """Reads the contents of a json file given by 'filepath' and returns
    properties as defined by 'selected_features'.
    """
    fo = open(filepath, 'r')
    raw_data = json.loads(fo.read())
    fo.close()
    # extract relevant data from json dict
    songs = raw_data.keys()
    properties = [k for k in raw_data[songs[0]].keys() if k in selected_features]
    props = [[float(v) for p, v in d.items() if p in selected_features] for (s, d) in raw_data.items()]
    # scale song properties to 0-1 interval
    mins = np.min(props, axis=0)
    maxs = np.max(props, axis=0)
    rng = maxs - mins
    props = 1 - (maxs - props) / rng
    return (songs, properties, dict(zip(songs, props)))
