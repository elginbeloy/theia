import time
import os

from selenium import webdriver
from termcolor import colored
from create_spectogram import create_spectrogram

# XPATHS
yt_music_recommended_song_xpath = '//div[@id="contents"]/ytmusic-player-queue-item'

# Text indicator to show before outputs
CRAWLER_INDICATOR = colored("[C R A W L E R] ", 'green')

# Crawl YoutubeMusic from seed URLs to create a list of potential 
# recommendation songs. Download and convert this list to spectograms.
def crawl_song_spectograms(seed_urls, crawler_depth=2, PAGE_LOAD_WAIT_TIME=5):
  print(f"{CRAWLER_INDICATOR} Starting URL search with the following parameters:")
  print(f"{CRAWLER_INDICATOR} Crawler Depth: {crawler_depth} videos")
  print(f"{CRAWLER_INDICATOR} Seed URLs: {seed_urls}")
  print(f"{CRAWLER_INDICATOR} Crawler Page Load: {PAGE_LOAD_WAIT_TIME}")
  print()

  # Start selenium session with Chrome driver
  print(f"{CRAWLER_INDICATOR} Starting Selenium headless Chrome instance...")
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('window-size=1920x1080')
  chrome_options.add_experimental_option("prefs", { 
      "profile.default_content_setting_values.notifications": 1 
  })
  driver = webdriver.Chrome('./chromedriver', options=chrome_options)
  print(f"{CRAWLER_INDICATOR} Complete!")
  print(f"{CRAWLER_INDICATOR} Cycling through seed URLs with a depth of {crawler_depth}!")
  print()

  scrapped_songs = {}
  for url in seed_urls:
      print(f"{CRAWLER_INDICATOR} Going to {url}...")
      # Get URL and wait for page to load (JavaScript & SPAs)
      driver.get(url)
      time.sleep(PAGE_LOAD_WAIT_TIME)

      print(f"{CRAWLER_INDICATOR} Grabbing recommended content for parsing...")
      set_size_before = len(scrapped_songs)
      recommended_song_elms = driver.find_elements_by_xpath(yt_music_recommended_song_xpath)
      for song_elm in recommended_song_elms:
        song_name = song_elm.find_element_by_xpath('.//yt-formatted-string[contains(@class, "song-title")]').text
        artist_name = song_elm.find_element_by_xpath('.//yt-formatted-string[contains(@class, "byline")]').text
        song_id = song_name.replace(' ', '')
        if song_id and song_name and artist_name:
          scrapped_songs[song_id] = {'name': song_name, 'artist': artist_name}

      print(f"{CRAWLER_INDICATOR} Added an additional {len(scrapped_songs) - set_size_before} unique songs!")
      print()

  print("{CRAWLER_INDICATOR} Downloading crawled songs from ytmp3.cc...")
  for song_id, song in scrapped_songs.items():
    # Go get the YT video URL for the song
    driver.get(f"https://www.youtube.com/results?search_query={song['artist']} {song['name']}")
    song['url'] = "https://www.youtube.com" + driver.find_element_by_id('video-title').get_attribute('href')
    print(f"{CRAWLER_INDICATOR} URL scrapped for {song['name']} - {song['artist']} ({song['url']})")

    # Go pirate the mp3 
    driver.get('https://ytmp3.cc/en13/')
    time.sleep(PAGE_LOAD_WAIT_TIME)
    print(f"{CRAWLER_INDICATOR} Grabbing song clip from ytmp3.cc...")

    # Type in the url and download it locally
    input_elm = driver.find_element_by_xpath("//input[@id='input']")
    input_elm.send_keys(song['url'])
    convert_button = driver.find_element_by_xpath("//input[@id='submit']")
    convert_button.click()
    
    downloaded = False
    conversion_time_seconds = 0
    while not downloaded:
      try:
        error = driver.find_element_by_id('error').text
        if (error):
          print(f"{CRAWLER_INDICATOR} got an error: {error}")
          break
      except:
        try:
          download_button = driver.find_element_by_link_text('Download')
          download_button.click()
          downloaded = True
        except:
          if conversion_time_seconds > 20:
            print(f"{CRAWLER_INDICATOR} Took too fucking long.")
            break
          print('Waiting on mp3 conversion...')
          conversion_time_seconds += 1
          time.sleep(1)

    if not downloaded:
      continue

    print('Waiting on mp3 download...')  
    time.sleep(5)
    filename = max([f for f in os.listdir('../Downloads')], key=lambda xa : os.path.getctime(os.path.join('../Downloads', xa)))
    while 'crdownload' in filename:  
      print('...waiting on mp3 download...')
      time.sleep(1)
      filename = max([f for f in os.listdir('../Downloads')], key=lambda xa : os.path.getctime(os.path.join('../Downloads', xa)))

    normalized_name = song['name'].replace(' ', '_').lower()
    normalized_artist = song['artist'].replace(' ', '_').lower()

    # Move the download to this folder and create spectogram
    print('Generating spectogram for song...')
    os.rename(os.path.join('../Downloads', filename), f"./songs/{normalized_name}__{normalized_artist}.mp3")
    create_spectrogram(f'{normalized_name}__{normalized_artist}', f'./songs/{normalized_name}__{normalized_artist}.mp3')
    

  print(f"{CRAWLER_INDICATOR} Complete!")
  print(f"{CRAWLER_INDICATOR} {len(scrapped_songs)} song spectograms created.")
