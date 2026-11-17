# 09. Glitch in the System

- **Local folder:** `/workspace/suno/09_glitch_in_the_system/` (on the original machine, not in this repo)
- **Publication status:** Published (inferred)
- **Date:** between 2026-10-31 and 2026-11-04 (exact date unknown)
- **Notes:** Inferred from per-playlist live counts on Nov 5 and local files (mp4 + cover built); YouTube URL not recorded. Verify in YouTube Studio. Suno clip version 1 chosen (2:02).
- **INDEX.txt lines:** `09_glitch_in_the_system | Glitch in the System | style: 347 | lyrics: 675`

## Suno inputs

### Title

```
Glitch in the System
```

### Lyrics

```
[Intro vocal: robotic vocoder male, dry, almost no beat]
Same street. Same cat.
Same tail. Same turn.
Twice in a minute.
Somebody missed a line.

[Build: stuttering clicks, vocoder repeats]
Run it back, run it back...

[DROP 1: glitchy minimal groove, short bright female hook]
Did you see it?

[Break: beat drops out, vocoder male alone, bitcrushed]
The sky has a seam.
The news has a loop.
If the walls repeat,
the walls are not real.

[Build 2: rising glitch, female hook doubled]
Look again, look again...

[DROP 2: full groove, bright female hook over vocoder]
Did you see it? I saw it!
Question everything.

[Outro: vocoder fades, one click left]
Same street. Same cat.
```

### Style of Music

```
Glitch minimal techno, 123 BPM, D minor, punchy short kick, sidechained sub bass, stuttering hi-hats, buffer repeat and tape-stop effects, thin square-wave arp, robotic vocoder male verses, bright clear female hook, vocal intro then first drop, second vocal break then bigger second drop, deadpan, curious, witty mood, clean sparse mix, club-ready
```

### Exclude Styles

```
pop chorus, rap, autotune, trap hi-hats, rock guitar, orchestral, heavy reverb
```

## YouTube video

### Video title

```
Glitch in the System | High-Tech Minimal Techno
```

### Storytelling description (story file)

```
Same street. Same cat. Twice in a minute. Did you see it?
#minimaltechno #hightechminimal #techno

It's an ordinary evening on an ordinary street. A cat crosses in front of a man, flicks its tail and turns the corner. He walks on. A minute later the same cat crosses again. Same street, same tail, same turn, the exact same flick. Somewhere, somebody missed a line in the script. Run it back.

Now he can't stop seeing it. The sky has a seam if you look long enough. The news plays the same story on a loop with a different face. And if the walls keep repeating, maybe the walls were never real. Most people blink and keep walking. He stops, looks again, and asks out loud. And somewhere a clear voice answers: I saw it too. That's how a glitch works. It only matters to the ones who notice. So keep your eyes open and question everything. Did you see it?

Sound: 123 BPM glitch minimal techno in D minor, punchy short kick, sidechained sub bass, stuttering hi-hats, buffer-repeat and tape-stop effects, a thin square-wave arp, robotic vocoder male verses and a bright, clear female hook.

More High-Tech Minimal in the playlist on this channel.

Music created with Suno AI. Concept, story and creative direction by the channel owner.

#glitchtechno #minimal #questioneverything #aimusic #electronicmusic #clubmusic
```

**Local build files (not in repo):** `/workspace/youtube/09_glitch_in_the_system.cover.png`, `/workspace/youtube/09_glitch_in_the_system.mp4`, `/workspace/youtube/09_glitch_in_the_system.title.txt`

## Suno version choice note

```
Glitch in the System - version choice (measurable checks only; nobody has listened)
Analysed 2026-10-31 with ffprobe/ffmpeg (silencedetect, volumedetect, ebur128, 0.25 s RMS profile of last 5 s).

v1 (audio/09_v1.mp3)
- Duration 121.58 s (2:02). Just inside the preferred 2:00-4:30 window.
- Silence: none mid-track (checked at -50 dB/1 s and -40 dB/0.5 s). Only the ending silence from 120.3 s.
- Loudness: integrated -14.7 LUFS, LRA 5.3 LU, mean -15.4 dB, peak -3.2 dB.
- Ending: full level (~-13.5 dB RMS) until ~117.8 s, then decays to -54 dB within 0.25 s and to -80/-90 dB, followed by ~1.2 s of silence. That's a clean, deliberate stop ("button" ending) with a release tail, not a cut-off. Last 1 s: mean -85.5 dB.

v2 (audio/09_v2.mp3)
- Duration 116.04 s (1:56). Under the preferred 2:00 minimum.
- Silence: none mid-track.
- Loudness: integrated -15.7 LUFS, LRA 3.0 LU, mean -17.1 dB, peak -4.5 dB.
- Ending: no fade and no tail. The level jumps to about -13 dB RMS ~0.9 s before the end, and the final 0.25 s is still at -22 dB RMS (last 0.3 s max -12.7 dB). The file stops while audio is still playing, which looks like an abrupt cut-off.

CHOICE: v1. It's within the duration window, has a clean ending with a decay and silent tail, is about 1 dB louder (closer to the -14 LUFS streaming reference), and has a wider dynamic range (more contrast between breaks and drops, as the song's two-drop structure needs). v2 fails on duration and ending.
Caveat: both versions are about 2 minutes. Measurement can't tell whether every lyric section made it in.
Winner copied to audio/09.mp3.
```

**Audio working copies (not in repo):** `/workspace/youtube/audio/09.mp3`, `/workspace/youtube/audio/09_v1.mp3`, `/workspace/youtube/audio/09_v2.mp3`
