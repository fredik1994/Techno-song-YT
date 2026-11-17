# 10. Wings of Air

- **Local folder:** `/workspace/suno/10_wings_of_air/` (on the original machine, not in this repo)
- **Publication status:** Published (inferred)
- **Date:** ~2026-11-04 (exact date unknown)
- **Notes:** Inferred from per-playlist live counts on Nov 5 and local files; YouTube URL not recorded. Verify in YouTube Studio. Suno clip version 2 chosen (3:22).
- **INDEX.txt lines:** `10_wings_of_air | Wings of Air | style: 385 | lyrics: 632`

## Suno inputs

### Title

```
Wings of Air
```

### Lyrics

```
[Intro vocal: fragile, breathy female, almost no beat]
I was born behind bars,
I sang to the bars.
I thought the world
was the size of my song.

[Build: riser, wingbeat flutters]
Push the door... push the door...

[DROP 1: melodic main beat, short wordless rise then one word]
Open.

[Break: beat drops out, voice getting stronger]
The latch was never locked.
It never was.
The only thing holding the door
was me.

[Build 2: voice now full and powerful]
Wings! Wings!

[DROP 2: full beat, powerful voice]
Wings of air! I'm out!
The cage was only fear.

[Outro: strings and air, soft again]
I was born behind bars.
I live in the sky.
```

### Style of Music

```
Melodic techno, 121 BPM, E minor, soft kick growing harder, warm bassline, string-like pads, fluttering pluck arpeggio like wingbeats, airy flute synth, wind swells, female vocal that starts fragile and breathy and grows into a powerful open voice, vocal intro then first drop, second vocal break then bigger second drop, fragile to fierce, liberating, emotional, cinematic, club-ready
```

### Exclude Styles

```
pop chorus, rap, autotune, trap hi-hats, male lead, distorted bass
```

## YouTube video

### Video title

```
Wings of Air | Melodic Techno
```

### Storytelling description (story file)

```
She was born in a cage and thought the world was the size of her song. Then she pushed the door.
#melodictechno #techno #freedom

A small bird is born behind bars. She has never known anything else, so she sings to the bars. Her song fills the cage, and she believes that is the whole world. Then one day she leans against the door. Push the door. Push the door. It opens.

The latch was never locked. It never was. The only thing holding the door shut was her own fear. Her voice starts fragile and breathy, then grows stronger with every beat until it's full and powerful, and she bursts into the open: Wings of air, I'm out. The cage was only fear. She was born behind bars. Now she lives in the sky. Whatever cage you think you're in, try the door. It may never have been locked.

Sound: 121 BPM melodic techno in E minor, a soft kick that grows harder, warm bassline, string-like pads, a fluttering pluck arpeggio like wingbeats, airy flute synth, wind swells, and a female vocal that starts fragile and breathy and grows into a powerful open voice.

More Melodic Techno in the playlist on this channel.

Music created with Suno AI. Concept, story and creative direction by the channel owner.

#melodic #wingsofair #aimusic #electronicmusic #clubmusic #emotionaltechno
```

**Local build files (not in repo):** `/workspace/youtube/10_wings_of_air.cover.png`, `/workspace/youtube/10_wings_of_air.mp4`, `/workspace/youtube/10_wings_of_air.title.txt`

## Suno version choice note

```
Wings of Air - version choice (measurable checks only; nobody has listened)
Analysed 2026-11-04 with ffprobe/ffmpeg (silencedetect -50 dB/2 s, ebur128, 0.25 s RMS profile of the last 6 s).

v1 (audio/10_v1.mp3)
- Duration 198.67 s (3:19). Inside the preferred 2:30-4:30 window.
- Silence: none over 2 s mid-track.
- Loudness: integrated -15.2 LUFS, LRA 6.2 LU.
- Ending: the last 6 s keep pulsing (-21 to -29 dB RMS) and only reach -33 dB in the final 0.25 s. The fade is still going when the file ends, so the tail looks slightly clipped.

v2 (audio/10_v2.mp3)
- Duration 201.98 s (3:22). Inside the window.
- Silence: none over 2 s mid-track.
- Loudness: integrated -15.1 LUFS, LRA 5.4 LU.
- Ending: smooth, steady fade from -22 dB to -39 dB over the last 6 s. That's a natural fade-out (fits the soft "strings and air" outro).

CHOICE: v2. Both pass duration, silence and loudness. v2 has the cleaner, more complete fade-out and is marginally louder. v1 has a bit more dynamic range but its tail ends while the fade is still in progress.
Caveat: both are about 3:20, shorter than the 5.6 min brief. Measurement can't confirm every lyric section is present.
Winner copied to audio/10.mp3.
```

**Audio working copies (not in repo):** `/workspace/youtube/audio/10.mp3`, `/workspace/youtube/audio/10_v1.mp3`, `/workspace/youtube/audio/10_v2.mp3`
