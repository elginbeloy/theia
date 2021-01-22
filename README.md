# T H E I A

Builds a list of recommended songs from MP3s by 
1. crawling Youtube Music for potential songs
2. downloading songs as MP3s
3. creating mel-spectograms from said downloaded MP3s, 
4. running a CNN trained to classify music genres but instead of classification we take the final output layer as a latent feature vector representing our song. we do this for 15 second samples.
5. creating a ranked list based on the distance from the songs and our recommending MP3 file

## Results (FIBONACCI4LOVE)

Below are the recommendation lists for 3 different FIBONACCI4LOVE songs. 
Results are based on `1,350` different song samples. We show all of the 
songs that rank higher than the other two FIBONACCI4LOVE samples. This 
means these songs are theoretically closer in instrumentation and mood
than even other FIBONACCI4LOVE songs. This is more telling than an 
abstract and contrived number than, for instance, top ten or five 
highest ranked.

> NOTE: More songs can be scrapped as needed later on.

### Dior:
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
Song: Life Is Good (Feat. Drake) (Future) with affinity value of 0.9904984879557077
Song: Blueberry Faygo (Lil Mosey) with affinity value of 0.9901346842340575
Song: Crazy Story (King Von) with affinity value of 0.9901180999577988
Song: Bop (Dababy) with affinity value of 0.9893856681376038
Song: Walk (Feat. Lil Baby & 42 Dugg) (Rylo Rodriguez) with affinity value of 0.9890630535625065
Song: Rockstar (Feat. Roddy Ricch) (Dababy) with affinity value of 0.9888511123608696
Song: Nothing To Lose (!!!FIBONACCI4LOVE!!!) with affinity value of 0.9883620691249796 <------ First FIBONACCI4LOVE
```


### Nothing To Lose:
```
Song: Life Is Good (Feat. Drake) (Future) with affinity value of 0.9963661339549892
Song: Suge (Dababy) with affinity value of 0.9956820906121026
Song: Bop (Dababy) with affinity value of 0.9949073171589554
Song: Walk (Feat. Lil Baby & 42 Dugg) (Rylo Rodriguez) with affinity value of 0.993219315529073
Song: Free Woo (42 Dugg) with affinity value of 0.9930017600801024
Song: Rockstar (Feat. Roddy Ricch) (Dababy) with affinity value of 0.9919531427853321
Song: Woah (Lil Baby) with affinity value of 0.9919281164779267
Song: Crazy Story (King Von) with affinity value of 0.9917400485788063
Song: Wow. (Post Malone) with affinity value of 0.9904229057730609
Song: 2Tone - Barbie (Official Video) (2Tone) with affinity value of 0.9902924324469711
Song: On Me (Lil Baby) with affinity value of 0.9894633952760192
Song: Cb So Easy (Prod By. Lfinguz) (@Chillimikevisuals) (The Official Cb) with affinity value of 0.9891990758885162
Song: All Love (Lil Durk) with affinity value of 0.9890077620945179
Song: Dior (FIBONACCI4LOVE) with affinity value of 0.9883620398480055 <------ First FIBONACCI4LOVE
```

### Dirty Laundry:

```
Song: Suicidal (Remix) (Feat. Juice Wrld) (Ynw Melly) with affinity value of 0.9946415240259481
Song: Lemonade (Feat. Nav) (Internet Money) with affinity value of 0.9755418897047364
Song: Falling (Trevor Daniel) with affinity value of 0.9734294242745002
Song: Fashionably Late (Thutmose) with affinity value of 0.9702968037045566
Song: Sunday Best (Surfaces) with affinity value of 0.9605563677325428
Song: Hot Girl Bummer (Blackbear) with affinity value of 0.9604374790909764
Song: Trust Nobody ($Tupid Young) with affinity value of 0.9590043869811513
Song: Donnyace- Next Level Mobile Cinematography | Birthday Highlight By Donnyace (Donnyace) with affinity value of 0.9546981894005453
Song: Wishing Well (Juice Wrld) with affinity value of 0.9530033232154801
Song: Iamsu! Ft. Jt The 4Th, Mayuex - Rings [Prod. By Juneonnabeat] [New 2018] (Kgbeatz) with affinity value of 0.9506431785616185
Song: Valentino (24Kgoldn) with affinity value of 0.9502527606478463
Song: Lucid Dreams (Juice Wrld) with affinity value of 0.9480460642615288
Song: Mood (Feat. Iann Dior) (24Kgoldn) with affinity value of 0.9431733747677742
Song: Down Below (Roddy Ricch) with affinity value of 0.94010846295007
Song: Highest In The Room (Travis Scott) with affinity value of 0.9400091239228192
Song: Better Now (Post Malone) with affinity value of 0.9368238679206674
Song: Can’T Feel My Face (The Weeknd) with affinity value of 0.9353545326993197
Song: Trap Queen (Fetty Wap) with affinity value of 0.9337159169643563
Song: No Guidance (Feat. Drake) (Chris Brown) with affinity value of 0.9335478403175589
Song: Sugar (Feat. Francesco Yates) (Robin Schulz) with affinity value of 0.9293804521033956
Song: Smile (Feat. The Weekend) (Juice Wrld) with affinity value of 0.9293071021501974
Song: Roses Remix (Feat. Future) (Saint Jhn) with affinity value of 0.9285696412999986
Song: Ballin’ (Feat. Roddy Ricch) (Mustard) with affinity value of 0.9260625605178093
Song: Mama Cry (Ynw Melly) with affinity value of 0.9231342281214977
Song: Dancin (Krono Remix) (Aaron Smith) with affinity value of 0.922983992832131
Song: Laugh Now Cry Later (Feat. Lil Durk) (Drake) with affinity value of 0.9219247895146293
Song: Low Life (Feat. The Weeknd) (Future) with affinity value of 0.9174296510084955
Song: Pure Water (Mustard) with affinity value of 0.9169439451542568
Song: Goodbyes (Feat. Young Thug) (Post Malone) with affinity value of 0.9158634163630199
Song: Mood Swings (Feat. Lil Tjay) (Pop Smoke) with affinity value of 0.9152010266269454
Song: Prayer In C (Robin Schulz Remix) - Radio Edit (Lilly Wood & The Prick & Robin Schulz) with affinity value of 0.9150737965442614
Song: Robbery (Juice Wrld) with affinity value of 0.9141944464111423
Song: Moonlight (Xxxtentacion) with affinity value of 0.9137075320461276
Song: Habits (Stay High) (Hippie Sabotage Remix) (Tove Lo) with affinity value of 0.9133861959471239
Song: 24 (Feat. Lil Baby) (Money Man) with affinity value of 0.9128843553785088
Song: Psycho (Feat. Ty Dolla $Ign) (Post Malone) with affinity value of 0.9127661406598245
Song: City Of Angels (24Kgoldn) with affinity value of 0.9117786043628598
Song: Teecee4800 - That'S What They All Say [New 2015] (Kgbeatz) with affinity value of 0.9111440397443972
Song: My Ex'S Best Friend (Machine Gun Kelly) with affinity value of 0.9090413967853581
Song: Mo Bamba (Sheck Wes) with affinity value of 0.909038988593232
Song: Plug Walk (Rich The Kid) with affinity value of 0.9087637331938676
Song: All Girls Are The Same (Juice Wrld) with affinity value of 0.9053115206290069
Song: Get Lucky (Feat. Pharrell Williams & Nile Rodgers) (Pharrell Williams & Nile Rodgers) with affinity value of 0.9050463563492127
Song: Come & Go (Feat. Marshmallow) (Juice Wrld) with affinity value of 0.9047604254144345
Song: Cb So Easy (Prod By. Lfinguz) (@Chillimikevisuals) (The Official Cb) with affinity value of 0.9047188986803697
Song: The Scotts (The Scotts, Travis Scott & Kid Cudi) with affinity value of 0.904694630485361
Song: Wow. (Post Malone) with affinity value of 0.9046900764694905
Song: F*Ck You, Goodbye (Feat. Machine Gun Kelly) (The Kid Laroi) with affinity value of 0.9041235776937643
Song: Blueberry Faygo (Lil Mosey) with affinity value of 0.9039969206047959
Song: I Feel It Coming (Feat. Daft Punk) (The Weeknd) with affinity value of 0.9024788793063095
Song: Sad! (Xxxtentacion) with affinity value of 0.9007840453402052
Song: Still Trappin' (King Von & Lil Durk) with affinity value of 0.8990886277830369
Song: For A Fact (King Von & Sim Santana) with affinity value of 0.8990886048490554
Song: Ispy (Feat. Lil Yachty) (Kyle) with affinity value of 0.8977103477983974
Song: Ocean Drive (Duke Dumont) with affinity value of 0.8969762042422326
Song: Butterfly Effect (Travis Scott) with affinity value of 0.8961540744059592
Song: That’S It (Future & Lil Uzi Vert) with affinity value of 0.8946828701072448
Song: Roxanne (Arizona Zervas) with affinity value of 0.8946206963387
Song: Wake Up In The Sky (Gucci Mane) with affinity value of 0.8944251082831094
Song: Rockstar (Feat. 21 Savage) (Post Malone) with affinity value of 0.8935480969644928
Song: Xo Tour Llif3 (Lil Uzi Vert) with affinity value of 0.8930181268755049
Song: Let'S Love (David Guetta) with affinity value of 0.8922341525967429
Song: Stupid Love (Lady Gaga) with affinity value of 0.8918274717105266
Song: The Box (Roddy Ricch) with affinity value of 0.8909767875646726
Song: Blinding Lights (The Weeknd) with affinity value of 0.8909268521108415
Song: Around (Youngboy Never Broke Again) with affinity value of 0.8885712448363322
Song: I Took A Pill In Ibiza (Seeb Remix) (Mike Posner) with affinity value of 0.8884342553815396
Song: In Your Eyes (The Weeknd) with affinity value of 0.8875420879881888
Song: Blame (Feat. John Newman) (Calvin Harris) with affinity value of 0.8875244246157866
Song: Be Like That (Feat. Swae Lee & Khalid) (Kane Brown) with affinity value of 0.8872557833301262
Song: Walk Em Down (Feat. Roddy Ricch) (Nle Choppa) with affinity value of 0.8827298652293433
Song: Baby (Quality Control, Lil Baby & Dababy) with affinity value of 0.8785791045283533
Song: My Way (Calvin Harris) with affinity value of 0.8780615479520041
Song: King Von - Grandson For President (Remix) (Official Video) (King Von) with affinity value of 0.8761503405427102
Song: Watermelon Sugar (Harry Styles) with affinity value of 0.8745010981639808
Song: Taj-He-Spitz - Bear (Taj-He-Spitz) with affinity value of 0.8712113180334873
Song: Sicko Mode (Travis Scott) with affinity value of 0.870107961899504
Song: The Voice (Lil Durk) with affinity value of 0.8693425543090147
Song: Dior (FIBONACCI4LOVE) with affinity value of 0.8689354958570723 <------ First FIBONACCI4LOVE
```