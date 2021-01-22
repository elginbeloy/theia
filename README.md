# T H E I A

Builds a list of recommended songs from MP3s by 
1. crawling Youtube Music for potential songs
2. downloading songs as MP3s
3. creating mel-spectograms from said downloaded MP3s, 
4. running a CNN trained to classify music genres but instead of classification we take the final output layer as a latent feature vector representing our song. we do this for 15 second samples.
5. creating a ranked list based on the distance from the songs and our recommending MP3 file

# Results (FIBONACCI4LOVE)

Below are the recommendation lists for 3 different FIBONACCI4LOVE songs. 
Results are based on `1,350` different song samples. We show all of the 
songs that rank higher than the other two FIBONACCI4LOVE samples. This 
means these songs are theoretically closer in instrumentation and mood
than even other FIBONACCI4LOVE songs. This is more telling than an 
abstract and contrived number than, for instance, top ten or five 
highest ranked.

> NOTE: More songs can be scrapped as needed later on.

Dior:

```
Song: 2Tone - Barbie (Official Video) (2Tone) with affinity value of 0.9978736121645492
Song: On Me (Lil Baby) with affinity value of 0.9972860799359465
Song: Around (Youngboy Never Broke Again) with affinity value of 0.9962742424270346
Song: Walk Em Down (Feat. Roddy Ricch) (Nle Choppa) with affinity value of 0.9960228144645836
Song: Be Like That (Feat. Swae Lee & Khalid) (Kane Brown) with affinity value of 0.995741859718615
Song: Suge (Dababy) with affinity value of 0.9955340147026386
Song: Woah (Lil Baby) with affinity value of 0.993166995097991
Song: Cb So Easy (Prod By. Lfinguz) (@Chillimikevisuals) (The Official Cb) with affinity value of 0.9929144070688594
Song: Baby (Quality Control, Lil Baby & Dababy) with affinity value of 0.9923556090479293
Song: Ispy (Feat. Lil Yachty) (Kyle) with affinity value of 0.9908503159908967
Song: Life Is Good (Official Music Video) (Feat. Drake) (Future) with affinity value of 0.9904984888880731
Song: Life Is Good (Feat. Drake) (Future) with affinity value of 0.9904984879557077
Song: Blueberry Faygo (Lil Mosey) with affinity value of 0.9901346842340575
Song: Crazy Story (King Von) with affinity value of 0.9901180999577988
Song: Bop (Dababy) with affinity value of 0.9893856681376038
Song: Walk (Feat. Lil Baby & 42 Dugg) (Rylo Rodriguez) with affinity value of 0.9890630535625065
Song: Rockstar (Feat. Roddy Ricch) (Dababy) with affinity value of 0.9888511123608696
Song: Nothing To Lose (!!!FIBONACCI4LOVE!!!) with affinity value of 0.9883620691249796 <------ First FIBONACCI4LOVE
```


Nothing To Lose:

```

```

Dirty Laundry:

