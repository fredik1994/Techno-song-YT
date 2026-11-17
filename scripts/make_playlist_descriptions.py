D = "Music created with Suno AI. Concept, story and creative direction by the channel owner."
P = [
("01_high_tech_minimal","High-Tech Minimal",
"Small sounds, sharp ideas. Notice the glitch, then step through it.",
"Clean, playful and witty minimal techno: dry tight kicks, rubbery bass, clicky micro-percussion and sparse vocals with short chopped hooks. Lots of space, every sound placed with a wink.",
"Every track is a tiny story about seeing through the system: curious creatures, cracks in the everyday and small brave choices that quietly build a freer world.",
"For deep focus, coding and late-night work sessions, or for anyone who likes their techno minimal and a little mischievous.",
"#minimaltechno #hightechminimal #techno #glitchtechno #focusmusic #aimusic"),
("02_melodic_techno","Melodic Techno",
"Follow the needle north. The exit was always there.",
"Emotional, atmospheric melodic techno: deep rolling kicks, pulsing analog bass, wide shimmering pads and glassy arpeggios under ethereal, intimate voices. Music that feels like cold air and open sky.",
"The stories here are about finding your way out of the maze: a compass that always points to the North Pole, open cage doors and the quiet courage to leave fear behind.",
"For night drives, long walks, reflection and focus, or anytime you need to feel something real.",
"#melodictechno #techno #deeptechno #progressivetechno #northpole #nightdrive #aimusic"),
("03_peak_time_techno","Peak-Time Techno",
"Wake up. It is time.",
"Driving, high-energy club techno built for the main room: big rumbling kicks, relentless offbeat bass, storm-sized stabs and short, punchy vocal hooks made to be shouted back.",
"Each track is a call to wake up. The system runs on attention and fear, and this music is about the moment people stop feeding it and remember how loud and powerful they are together.",
"For the gym, running, pre-game and the peak of the night, whenever you need pure energy.",
"#peaktimetechno #techno #warehousetechno #rave #gymmusic #workoutmusic #aimusic"),
("04_japanese_techno","Japanese Techno",
"No master. No banner. Only the road.",
"Techno forged with Japanese colour: heavy kicks and rolling bass meet taiko drums, shakuhachi breath, koto plucks and chanted vocals with a few Japanese words.",
"The stories come from samurai, ronin, katana and dragon legends, retold as lessons in freedom: serve no one but your truth, let pain shape your strength and wake the power sleeping inside you.",
"For training, martial arts, gaming and focused work, or for fans of samurai cinema and cyberpunk.",
"#japanesetechno #techno #samurai #ronin #katana #darktechno #aimusic"),
("05_dark_techno","Dark Techno",
"Feel the strings? Look up.",
"Hypnotic, mysterious dark techno: deep rumbling kicks, droning sub bass, sparse metallic hits, warped textures and low whispered voices that pull you further in.",
"This is the home of the deception theme. Puppet strings, mazes, shadows on the wall and the matrix that runs on fear. Every track ends the same way: you see the trick, and you are free of it.",
"For late nights, headphones, dark rooms and deep concentration, or for underground warehouse energy.",
"#darktechno #hypnotictechno #undergroundtechno #industrialtechno #techno #matrix #aimusic"),
("06_euphoric_techno","Euphoric Techno",
"Let it burn. Then rise.",
"Uplifting, goosebump techno: powerful kicks, blazing lead melodies, choir pads, giant risers and soaring vocals that hold back before a full release.",
"These tracks are about the moment fear lets go: rebirth from the ashes, the northern lights as an open gate at the North Pole and a humanity that wakes up and remembers it is free, many and powerful.",
"For festivals, sunrise sets, workouts and big moments, or whenever you need hope turned up loud.",
"#euphorictechno #upliftingtechno #festivaltechno #melodictechno #techno #motivation #aimusic"),
("07_ethnic_techno","Ethnic Techno",
"Nobody gave you this fire, and nobody can take it.",
"Hypnotic techno woven with the melodies of the Middle East, Persia, Anatolia, Arabia and Central Asia: driving kicks, frame drums, tar, kamancha and saz colours, maqam ornaments and ornamented Eastern vocal runs over ritual chants.",
"The stories travel the old caravan roads of many lands. Myths of fire, deserts and ancient wisdom, retold as one message: your inner fire was here before the fear, and it outlasts every ruler.",
"For long drives, deep focus, meditation and late-night dancing, or for anyone who loves Eastern sound with a modern pulse.",
"#ethnictechno #middleeasterntechno #orientaltechno #persian #anatolian #tribaltechno #aimusic"),
("08_afro_techno","Afro Techno",
"Sit in the circle. The drum is talking.",
"Rhythm-first techno with tribal energy: warm deep kicks, rolling sub bass, layered hand drums, shakers, hypnotic melodic motifs and call-and-response chants.",
"The stories are about healing and connection: drums that lift grief, courage that grows in the storm and voices of the ancestors that remind you that you are never alone and never powerless.",
"For dancing, running, workouts and sunset sessions, or anytime you want to feel the groove in your body.",
"#afrotechno #afrohouse #tribaltechno #ritualtechno #techno #percussion #aimusic"),
]
allmd=["# YouTube playlist descriptions (8 playlists)\n"]
for f,n,h,s,st,w,tags in P:
    t="\n\n".join([h,s,st,w,D,tags])
    assert "<" not in t and ">" not in t and "zerbaij" not in t.lower()
    assert 500<=len(t)<=900, (n,len(t))
    open(f+".txt","w").write(t+"\n")
    allmd.append(f"## {n}  ({len(t)} chars)\n\n```\n{t}\n```\n")
    print(n,len(t))
open("ALL.md","w").write("\n".join(allmd))
