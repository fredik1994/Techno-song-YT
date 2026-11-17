# Daily release routine (tool-neutral rewrite of the automation's exact instructions)

This is the instruction set that a scheduled automation ("routine") in Grok Bot ran every day. It is rewritten here so any AI tool or human can follow it. Nothing from the original has been dropped; where the original named a Grok Bot–specific tool, the neutral equivalent is given and the original term is in parentheses.

## Routine metadata (original)

- Name: "Techno release: generate and publish next song" (id `techno-release-generate-and-publish-next-song`), enabled until the end of the test.
- Schedule: every day at 10:00, time zone Asia/Baku (UTC+4), flexible ±15 min (the server actually picked 10:10). Cron form: `CRON_TZ=Asia/Baku 0 10 * * *`.
- Owner: Farid Mammadov. He has **waived per-song approval**: each run generates and publishes the next techno song on his YouTube channel (**Мu Zone**, with a Cyrillic М) end to end, without asking him first.
- Cadence: as of 2026-11-04 he chose **ONE song per day for 2 weeks (2026-11-05 to 2026-11-18)**, then a performance review.
- If today is **after 2026-11-18**: do NOT publish. Instead pause the routine, gather basic performance numbers (views, watch time) for all videos on the channel through YouTube Studio, and tell Farid the results with a recommendation for the next cadence.

## Steps

### 1. Pick the next song

- Rotate through the 8 playlists: High-Tech Minimal, Melodic Techno, Peak-Time Techno, Japanese Techno, Dark Techno, Euphoric Techno, Ethnic Techno, Afro Techno.
- Choose the playlist with the **fewest songs live**, and within it the **next unpublished song** in the master catalog order.
- Sources: the master catalog (66 songs) is `catalog/MASTER_CATALOG.md` in this repo (original: Grok Bot Page via ReadCanvas, canvas_id `2b472171-cc5c-4bf4-a7cd-dcee36546acf`). Per-playlist lyrics and production briefs are the files in `catalog/` (original Page ids in parentheses): High-Tech Minimal (`d56bcbe7-c0e9-4ba0-8fbd-c0f44d184ecd`), Melodic (`f674f280-7b66-422e-9590-a812378024bf`), Peak-Time (`e9fdfac7-59f0-4482-a818-efd8e56ccff1`), Japanese (`451c9da8-d415-4575-9ecc-b2988d4721e0`), Dark (`61e515f0-9cd5-4660-8cfb-59efa490f16f`), Euphoric (`464362f1-5af6-49a1-aae5-9a0aac3874d6`), Ethnic (`19a35d16-4cb0-4b2e-be60-dd697e86fb68`), Afro (`269afaf1-771f-411c-b045-4e397f681f88`).
- Use the catalog's saved lyrics and production brief. **Do not invent new songs** unless the catalog truly cannot be read.
- Originally the working folders were `/workspace/suno/` (one folder per generated song: title, lyrics, style, exclude files and INDEX.txt) and `/workspace/youtube/` (video builds). In this repo these are `songs/` (text) and `scripts/`.
- Check what is already live (see "Release log" in `HANDOFF.md`) before choosing so nothing is posted twice.
- If a run was missed, still publish just **one** song for today.

### 2. Research first, briefly

- At most once a week; reuse the notes in `research/techno_notes.md`.
- Look at publicly listed million-view techno tracks in that sub-genre: tempo, structure, intro length, drop timing, sound palette, title/thumbnail patterns, what viewers praise.
- Adjust the Suno style text accordingly. **Never copy** a melody, lyric, title or artist name. **Never reference artists** in Suno prompts.

### 3. Generate in Suno

- Use the saved lyrics, style and exclude text. Lyrics stay short and sparse: vocal intro, first drop, second vocal, second drop.
- Publish only **ONE** of Suno's two versions (Farid's rule).
- Choose from what the Suno page shows: duration 2:30–4:30, ideally ~3:15; title and lyrics match. Download only the chosen one.
- Download path (Suno's official menu): song page > "..." (More options) > Download > a format dialog opens; click **MP3**, and if the Download / "Unlock & Download" button stays grey, click **MP3 a SECOND time** (verified 2026-11-09), then click the button **once**. Do not trigger a second download (it burns allowance).
- Verify the downloaded file with ffmpeg: no silence gap > 2 s mid-track, no abrupt end, reasonable loudness (see HANDOFF.md workflow section for the exact commands).
- If it fails, download the other version; if both fail, regenerate once.
- If the button will not enable after the double click and a page reload, ask Farid for a handoff (he does the download in the shared browser).

### 4. Build and upload the video

- Build with ffmpeg: still cover image + MP3, `-t <audio duration>`, `-r 2`, **no `-shortest`**. Full command is in HANDOFF.md.
- Make a new cover in the style of `scripts/make_cover_*.py` with a distinct motif for each song.
- Write a storytelling description like those in `songs/*.md` (YouTube description sections).
- Upload to YouTube Studio as **Public**, set **AI use (altered/synthetic content disclosure) = Yes**, add it to its **existing** playlist (never create duplicate playlists), and verify by reloading the video page.

### 5. Shorts and mixes

- Cut 1 Short when practical (vertical, about 45 seconds, from the break into the second drop or from the second drop).
- When a playlist reaches about 8 songs, build its long mix video.
- (Standing preference from 2026-11-04: 3–4 Shorts per week from released songs, and a long mix per playlist at about 8 songs, rotating through the 8 playlists.)

### 6. Browser discipline

- Do browser work one step and one video at a time.
- YouTube Studio often asks for Google **password re-verification**: this needs Farid himself (the assistant never has the password). Ping Farid to complete it in the shared browser session.

### 7. Journal

- Save a journal note of what was published and what is next. (In this repo, update the Release log in `HANDOFF.md`.)

### Result message

Deliver a short result message to Farid after every run: title, playlist, YouTube link, which Suno version and why, anything needing him. If blocked, say what blocked it.

## Addenda learned during the test (not in the original saved prompt, but followed in practice since 2026-11-10)

- In Suno, **Duration "Auto" produced 1:59 songs** on 2026-11-10. Before generating, set a custom length under Create > Advanced > More Options > Duration = Custom (4:00 gave ~3:59; the original aim was ~3:15, so consider setting ~3:15–3:30).
- Many runs added a 3–4 s fade-out in the video when the track ended slightly abruptly (cheaper than spending another Suno download).
- Tempo nudges based on research were applied in the style text: Tuning Fork 121→124 BPM, Last Lighthouse →123, Fire Walker →130, Moon Eats the Sun 126, Aurora Gate 128, Desert Djinn 125.
- Suno download allowance is shared with another bot (Kids Songs Studio) and was down to about 7 on 2026-11-17 until it renews on 2026-11-28 — check "downloads left" in Suno before each run.
