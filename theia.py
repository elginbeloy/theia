import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 

import os
import numpy as np
import keras
import cv2
from PIL import Image
from keras.models import Model, load_model
from create_spectogram import create_spectrogram
from crawl_song_spectograms import crawl_song_spectograms
import cv2
from termcolor import colored

seed_urls = [
  'https://music.youtube.com/watch?v=JFm7YDVlqnI',
  'https://music.youtube.com/watch?v=cDde7QlKCX0',
  'https://music.youtube.com/watch?v=U0AK2RXJTQM',
  'https://music.youtube.com/watch?v=fHI8X4OXluQ',
  'https://music.youtube.com/watch?v=GAEuJe8NDzc',
  'https://music.youtube.com/watch?v=IxJjY5T9yag',
  'https://music.youtube.com/watch?v=hHtv2XMZlKs',
  'https://music.youtube.com/watch?v=74QWd6b9byk',
  'https://music.youtube.com/watch?v=FkXulkASrqc'
]

song_paths = {
  'nothing_to_lose': 'fibo_songs/nothing_to_lose.mp3',
  'dior': 'fibo_songs/dior.mp3',
  'dirty_laundry': 'fibo_songs/dirty_laundry.mp3',
}

# Create spectograms for Fibo's songs
for song_name in song_paths:
  create_spectrogram(song_name, song_paths[song_name])

# Load the genere-classifier trained model and discard the final Softmax layer.
# The layer prior to the last provides the latent feature representation.
loaded_model = load_model("saved_model/model.h5")
loaded_model.set_weights(loaded_model.get_weights())
matrix_size = loaded_model.layers[-2].output.shape[1]
new_model = Model(loaded_model.inputs, loaded_model.layers[-2].output)

user_input = input("Crawl Youtube Music? y/N: ")
if user_input == 'y':
  # Create the spectograms from YoutubeMusic then load them.
  crawl_song_spectograms(seed_urls)

filenames = [os.path.join("song_spectograms/", f) for f in os.listdir("song_spectograms") if "__slice-" in f]
images, labels = [], []
for f in filenames:
  label = f.split('__slice-')[0].replace('song_spectograms/', '')
  label.replace('song_spectograms/', '')
  labels.append(label)

  tempImg = cv2.imread(f, cv2.IMREAD_UNCHANGED)
  images.append(cv2.cvtColor(tempImg, cv2.COLOR_BGR2GRAY))

# Convert to numpy array and normalize.
images = np.array(images)
images = np.expand_dims(images, axis=3)
images = images / 255.

# Display list of available songs for recommendation.
song_options = []
for index, label in enumerate(np.unique(labels)):
  label_sections = label.split("__")
  song_options.append(label)

  output_str = f"{colored(index, 'blue')}. {label.split('__')[0].replace('_', ' ').title()}"
  if (len(label_sections)) > 1:
    output_str += " - " + colored(label.split('__')[1].replace('_', ' ').title(), "red")
    print(output_str)
  else:
    output_str += " - " + colored("FIBONACCI4LOVE", "green")
    print(output_str)

recommend_wrt = song_options[int(input("Enter Song Number: "))]
prediction_anchor = np.zeros((1, matrix_size))
sample_count = 0
predictions_song = []
predictions_label = []
counts = []
cosine_similarity_arr = []

# Calculate the latent feature vectors for all the songs.
for i in range(0, len(labels)):
  if(labels[i] == recommend_wrt):
      test_image = images[i]
      test_image = np.expand_dims(test_image, axis=0)
      prediction = new_model.predict(test_image)
      prediction_anchor = prediction_anchor + prediction
      sample_count = sample_count + 1
  elif(labels[i] not in predictions_label):
      predictions_label.append(labels[i])
      test_image = images[i]
      test_image = np.expand_dims(test_image, axis=0)
      prediction = new_model.predict(test_image)
      predictions_song.append(prediction)
      counts.append(1)
  elif(labels[i] in predictions_label):
      index = predictions_label.index(labels[i])
      test_image = images[i]
      test_image = np.expand_dims(test_image, axis=0)
      prediction = new_model.predict(test_image)
      predictions_song[index] = predictions_song[index] + prediction
      counts[index] = counts[index] + 1

# Average the latent feature vectors from the samples
prediction_anchor = prediction_anchor / sample_count
for i in range(len(predictions_song)):
    predictions_song[i] = predictions_song[i] / counts[i]
    # Cosine Similarity for each song w.r.t the anchor song.
    cosine_similarity_arr.append(np.sum(prediction_anchor * predictions_song[i]) / (np.sqrt(np.sum(prediction_anchor**2)) * np.sqrt(np.sum(predictions_song[i]**2))))

cosine_similarity_arr = np.array(cosine_similarity_arr)

print("Recommendations:")
recommendations = 0
while recommendations < len(cosine_similarity_arr):
    index = np.argmax(cosine_similarity_arr)
    
    affinity_value = cosine_similarity_arr[index]
    song_name = predictions_label[index].split('__')[0].replace('_', ' ').title()
    if (len(label.split('__'))) > 1:
      artist_name = label.split('__')[1].replace('_', ' ').title()
    else:
      artist_name = colored("FIBONACCI4LOVE", "green")
      
    print(f"Song: {song_name} ({artist_name}) with affinity value of {affinity_value}")

    cosine_similarity_arr[index] = -np.inf
    recommendations = recommendations + 1