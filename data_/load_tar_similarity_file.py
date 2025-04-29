import gzip
import pickle

with gzip.open('data_/similarity.pkl.gz', 'rb') as f:
    data = pickle.load(f)
