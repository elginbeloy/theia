import math
import librosa
import librosa.display
import matplotlib.pyplot as plt
from PIL import Image

# Converts an mp3 file into split mel-spectrograms.
def create_spectrogram(song_name, mp3_path):
  spectogram_path = f"song_spectograms/{song_name}__full.jpg"

  # Load file and generate mel spectorgram array.
  y, sr = librosa.load(mp3_path)
  melspectrogram_array = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
  mel = librosa.power_to_db(melspectrogram_array)
  
  # Display the spectogram on matplotlib plot and save it locally.
  fig_size = plt.rcParams["figure.figsize"]
  fig_size[0] = float(mel.shape[1]) / float(100)
  fig_size[1] = float(mel.shape[0]) / float(100)
  plt.rcParams["figure.figsize"] = fig_size
  plt.axis('off')
  plt.axes([0., 0., 1., 1.0], frameon=False, xticks=[], yticks=[])
  librosa.display.specshow(mel, cmap='gray_r')
  plt.savefig(spectogram_path, bbox_inches=None, pad_inches=0)
  plt.close()

  # Save 128px slices of the spectogram average distance comparison.
  img = Image.open(spectogram_path)
  subsample_size = 128
  width, height = img.size
  number_of_samples = width / subsample_size
  for i in range(math.floor(number_of_samples)):
    start = i*subsample_size
    img_temporary = img.crop((start, 0., start + subsample_size, subsample_size))
    img_temporary.save(f"song_spectograms/{song_name}__slice-{i}.jpg")