import numpy as np

# This just gets the filenames with speaker referenes (because it is not clear in the filename otherwise)
dataroot = '../../datasets/flickr_audio/flickr_audio/'
textin = dataroot + 'wav2spk.txt'
speaker_files = np.genfromtxt(textin, dtype=[('mystring','S27'),('myint','i8')], delimiter=' ')
spks = [spk for (filename, spk) in speaker_files]
spks_set = set(spks)
print(f"Number of unique speakers: {len(spks_set)}")
