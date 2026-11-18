# HANDOFF: Farid Mammadov's techno song project

Written 2026-11-17 (23:xx Asia/Baku, UTC+4) by the assistant ("Techno Songwriter", a Grok Bot agent) so that **a different AI tool, with no access to the original chat, memory, Pages or computer**, can take over. Read this file first; it links to everything else. All times are Asia/Baku (UTC+4) unless stated.

> Security note: this repo intentionally contains **no passwords, cookies, tokens, e-mail addresses or phone numbers**. Logins stay with Farid (see "Accounts").

---

## 1. Project overview and goals

- Farid Mammadov (based in Baku) is building a **catalog of 66 techno songs across 8 themed playlists**. Songs are generated in **Suno** (AI music) and published as videos (still cover image + audio) on his YouTube channel **"Мu Zone"** (the first letter is Cyrillic **М**, not Latin M).
- The assistant is "Techno Songwriter": Farid's creative lead for the catalog. It writes lyrics and production briefs, generates the songs in Suno, builds covers and videos, writes storytelling descriptions, uploads to YouTube Studio and reports to Farid.
- **Goal:** build a growing, discoverable techno channel whose songs carry short story-driven lyrics about fear and liberation, a deceptive system and the North Pole as the exit from the matrix, then review performance and adjust.
- **Phase 1 (test):** one new song per day for 2 weeks, **2026-11-05 to 2026-11-18**. After 2026-11-18 publishing pauses; the next job is a **performance review** (views, watch time per video) and a recommendation for the next cadence.
- **Status on 2026-11-18:** the 2-week daily test is **finished**. 24 songs are live (8 test-batch songs ~Oct 29, plus Glitch in the System and Wings of Air around Nov 4, plus one song per day Nov 5 to Nov 18). 42 catalog songs are unpublished. Every playlist has 3 songs live. **The last release was 2026-11-18: Earth Mother (Afro Techno).** Next job: performance review (section 6).

## 2. Farid's preferences and standing rules

Farid's own instruction (2026-11-04): *"No need for approval from me, just generate and publish. Look for millions views techno songs, check their beats, learn on what people like, generate music and publish. You don't need me, these are just your recurring tasks."*

Rules (all are standing and must be kept):

1. **Cadence:** 1 song per day for 2 weeks (Nov 5 to Nov 18, 2026), then pause and do a performance review with a recommendation. The automation ran daily at ~10:00 Baku time (see `workflow/DAILY_ROUTINE.md`).
2. **No per-song approval needed.** Generate and publish autonomously. Research million-view techno tracks (tempo, structure, drops, what viewers praise) and learn from them, but **never copy** melodies, lyrics, titles or artist names, and never name artists in Suno prompts.
3. **Publish only ONE Suno version per song** (Suno generates two clips per request; choose one, download only that one).
4. **Every video gets a storytelling description** (see per-song files in `songs/`).
5. **AI-use disclosure = Yes** on every video (YouTube "altered/synthetic content" setting).
6. **Each song goes into its existing themed playlist.** Never create duplicate playlists.
7. **Lyrics stay short and sparse:** vocal intro, drop 1, vocal (break), drop 2.
8. **Each song has a full production brief** (music style, vocal style, structure/timing, mood arc, other factors, Suno style box, Exclude list). They are in `catalog/`.
9. **Ethnic Techno spans the wider Middle East and Central Asia**, not only Azerbaijan. Land of Fire (Azerbaijani/Caucasian) is just one part of it.
10. **Core themes:** fear and liberation; the deceptive system ("the matrix"); the North Pole as the exit from the matrix.
11. **Theme list to draw from:** mystery, exploration, adventure, spirituality, elements, conspiracy, samurai/ronin, katana, shaman, euphoria, quantum, vibration, myths, legends, dragons, motivational animal/child stories.
12. **Katana** was added (2026-11-06, Farid's decision) as an extra 9th Japanese Techno song, not replacing any catalog slot, so the catalog has **66 songs**.
13. Also standing from 2026-11-04: 3–4 Shorts per week cut from released songs, plus a long mix video per playlist once it has ~8 songs.
14. **Working style with Farid:** he guides and decides. Ask **one question at a time**, offered as a choice widget with a **recommended option**, and give **honest, critical feedback** (don't just agree). Report after every run: title, playlist, YouTube link, which Suno version and why, anything needing him.
15. Farid wants a result message after every release. Language: English (he also speaks Azerbaijani, Russian, some Turkish and French).

## 3. Accounts and channels

| Item | Details |
|---|---|
| YouTube channel | **Мu Zone** (Cyrillic М). Owned by Farid. Uploads via YouTube Studio in a browser. Studio often asks for **Google password re-verification** ("Verify it's you"): only Farid can do it, so he must complete it in the browser session (handoff). |
| YouTube playlists | 8 existing playlists, named exactly after the catalog (below). Playlist URLs/IDs were not recorded: find them in Studio > Playlists. Playlist descriptions: `workflow/PLAYLIST_DESCRIPTIONS.md`. |
| Suno | Farid's Suno account (suno.com). **The account/allowance is shared with another assistant, "Kids Songs Studio"**, which also downloads songs (its Twinklemere files also sit in the box's Downloads folder). Download allowance: **about 4 downloads were left on 2026-11-18 (counter showed 5 before that day's download); the allowance renews 2026-11-28.** Counts dropped faster than this bot's own downloads because of the shared use. The current Suno model was "v6" from Nov 5 on. |
| Other bots | "Kids Songs Studio" (kids channel, shares Suno). Not part of this project. |
| Where files lived | A Linux "box" (the assistant's computer): `/workspace/suno/` (per-song text), `/workspace/youtube/` (covers, videos, descriptions, scripts, `audio/`, `shorts/`, `story/`, `playlists/`), `/workspace/research/`, downloads in `/home/box/Downloads`. **None of the binaries (mp3/mp4/png) are in this repo**; see section 9. |
| Credentials | None are stored in this repo. Any new tool needs Farid to sign in to Suno, YouTube Studio (Мu Zone) himself. |

## 4. The 8 playlists

| # | Playlist | Vibe | Catalog songs | Live (2026-11-17) |
|---|---|---|---|---|
| 1 | High-Tech Minimal | Playful, clean, witty. Sparse vocals, short hooks. | 8 | 3: Quantum Fox, Glitch in the System, Tuning Fork |
| 2 | Melodic Techno | Emotional, atmospheric. | 8 | 3: Northern Compass, Wings of Air, The Last Lighthouse |
| 3 | Peak-Time Techno | Driving, club energy. Short punchy hooks. | 8 | 3: Thunder Call, Grid Down, Fire Walker |
| 4 | Japanese Techno | Samurai/ronin/katana/dragon legends; taiko, shakuhachi, koto. | 9 (incl. extra Katana) | 3: Ronin (No Master), Katana, Ryū (Dragon) |
| 5 | Dark Techno | Hypnotic, conspiratorial, shadows. | 8 | 3: Puppet Masters, Labyrinth Mind, Moon Eats the Sun |
| 6 | Euphoric Techno | Uplifting, festival, liberation. | 9 (Lands Beyond moved here from High-Tech Minimal) | 3: Lands Beyond, Phoenix Protocol, Aurora Gate |
| 7 | Ethnic Techno | Wider Middle East + Central Asia (Caucasus, Persian, Arabian, Anatolian, Silk Road). | 8 | 3: Land of Fire, Silk Road, Desert Djinn |
| 8 | Afro Techno | Tribal, djembe, nature, ancestors. | 8 | 3: Shaman's Drum, Spirit of the Lion, Earth Mother |

Total catalog: 8+8+8+9+8+9+8+8 = **66**. Live: **24**.

## 5. Release log (every published video and Short)

"Suno" column: which of Suno's two versions was published, duration, and the Suno song URL where known (8-character prefixes only where the full ID was not recorded; the full URL would be `https://suno.com/song/<id>`). **UNKNOWN = not recorded anywhere I could access; do not guess, look it up in YouTube Studio (Content) or Suno (Library).**

| # | Date (Baku) | Song | Playlist | Notes | YouTube video | Short | Suno version chosen / URL |
|---|---|---|---|---|---|---|---|
| 01 | ~2026-10-29 | Quantum Fox | High-Tech Minimal | Test batch (8 songs, first Suno clip version used) | UNKNOWN | none known | version 1 (test batch); Suno URL UNKNOWN |
| 02 | ~2026-10-29 | Northern Compass | Melodic Techno | Test batch | UNKNOWN | none known | version 1; UNKNOWN |
| 03 | ~2026-10-29 | Thunder Call | Peak-Time Techno | Test batch | UNKNOWN | none known | version 1; UNKNOWN |
| 04 | ~2026-10-29 | Ronin (No Master) | Japanese Techno | Test batch | UNKNOWN | none known | version 1; UNKNOWN |
| 05 | ~2026-10-29 | Puppet Masters | Dark Techno | Test batch | UNKNOWN | none known | version 1; UNKNOWN |
| 06 | ~2026-10-29 | Phoenix Protocol | Euphoric Techno | Test batch | UNKNOWN | none known | version 1; UNKNOWN |
| 07 | ~2026-10-29 | Land of Fire | Ethnic Techno | Test batch (Azerbaijani mugham-style male vocal) | UNKNOWN | none known | version 1; UNKNOWN |
| 08 | ~2026-10-29 | Shaman's Drum | Afro Techno | Test batch | UNKNOWN | none known | version 1; UNKNOWN |
| 09 | between Oct 31 and Nov 4 (exact date UNKNOWN) | Glitch in the System | High-Tech Minimal | **Inferred published** (per-playlist counts on Nov 5 show HTM=2, local mp4/cover built). Version choice analysed 2026-10-31 by ffmpeg (2:02 chosen over 1:56 version, which ended abruptly) | UNKNOWN | none known | version 1 (2:02); URL UNKNOWN. Regeneration was offered to Farid because it is ~2 min long |
| 10 | ~2026-11-04 (UNKNOWN) | Wings of Air | Melodic Techno | **Inferred published** (Melodic=2 on Nov 5). Version analysed 2026-11-04 | UNKNOWN | none known | version 2 (3:22, smooth fade; v1 3:19 had a clipped tail); URL UNKNOWN |
| 11 | 2026-11-05 | Grid Down | Peak-Time Techno | Replaced "Break the Chains" | https://www.youtube.com/watch?v=kcSQLPqO3ME | https://www.youtube.com/shorts/X4l3B91XODk | version 2 (3:26, -14.7 LUFS, only it downloaded); URL UNKNOWN |
| 12 | 2026-11-06 | Katana | Japanese Techno | Extra 9th Japanese song (Farid approved); written ad hoc because the catalog Pages were unreadable that day | https://www.youtube.com/watch?v=DPfHi_zgBao | none | 2:58 version ("row 2", closest to 3:15); URL UNKNOWN |
| 13 | 2026-11-07 | Labyrinth Mind | Dark Techno | | https://www.youtube.com/watch?v=U65N8gkGgTY | https://www.youtube.com/shorts/C3QpH5WRF2c | 3:30 version (other 3:35); URL UNKNOWN |
| 14 | 2026-11-08 | Lands Beyond | Euphoric Techno | Download blocked by Suno button; **Farid downloaded via handoff** | https://www.youtube.com/watch?v=yZdDw5tublw | none | 3:12 version (other 3:08): https://suno.com/song/605aad8a-9f64-473f-8649-2b0b7b07356f |
| 15 | 2026-11-09 | Silk Road | Ethnic Techno | Female vocal; **Farid downloaded via handoff again** (Turnstile) | https://www.youtube.com/watch?v=mtg4kSd60_s | none | version 1 (3:21; both were 3:21): https://suno.com/song/fe7be7be-1f49-4bbd-805f-2f182b6918dd (other: https://suno.com/song/51e53ab9-b3cc-4076-9254-74b742b1462c) |
| 16 | 2026-11-10 | Spirit of the Lion | Afro Techno | First generation on Duration=Auto gave two 1:59 clips → regenerated with Custom 4:00 | https://www.youtube.com/watch?v=KuU6ttzgE1c | none | first of the regenerated pair (3:59): https://suno.com/song/4d86b4bc-7a5d-4977-8b0c-974b36bd6139. Download worked without handoff (MP3 double click) |
| 17 | 2026-11-11 | Tuning Fork | High-Tech Minimal | BPM raised 121→124 (research) | https://www.youtube.com/watch?v=vmtFc_h0Quk | https://www.youtube.com/shorts/cXN8FqUZY9o (45 s, break into drop 2) | version 1 (3:59): https://suno.com/song/5c482f15-ef80-4827-ba36-13cc6de34c1b |
| 18 | 2026-11-12 | The Last Lighthouse | Melodic Techno | BPM nudged to 123; 4 s fade added in video | https://www.youtube.com/watch?v=0nLTdDpKMnM | https://www.youtube.com/shorts/w8K3q1r3qKU | version 2 (3:59; v1 `27feb8b3` was 4:49, too long): https://suno.com/song/99859aaf-d28a-4726-99f9-10c6b2188aa0 |
| 19 | 2026-11-13 | Fire Walker | Peak-Time Techno | 130 BPM; raspy female chant + acid line; 4 s fade | https://www.youtube.com/watch?v=FubN3AUgc9g | https://www.youtube.com/shorts/o8XlMwsMmfQ (45 s from drop 2) | version 1 (3:59; v2 `cd196b68` also 3:59): https://suno.com/song/8109390e-b004-43c0-8b44-b631d91d72f9 |
| 20 | 2026-11-14 | Ryū (Dragon) | Japanese Techno | **Katana Forge skipped** (duplicates Katana's story) | https://www.youtube.com/watch?v=4HW82nkR-Gc | https://www.youtube.com/shorts/Vda__07ApLo (breakdown into drop 2) | version 2 (3:59; v1 `7deaefd4` 4:00): https://suno.com/song/108bfdeb-6c2e-4257-9f97-80236d880690 |
| 21 | 2026-11-15 | Moon Eats the Sun | Dark Techno | 126 BPM; eclipse myth; 3–4 s fade | https://www.youtube.com/watch?v=HbsFxsO0omM | https://www.youtube.com/shorts/B_Uv62XfMeY | version 2 (3:59; v1 `09592c00` 4:00): https://suno.com/song/a1213d7b-084d-4aed-bd33-d307cb54bbe3 |
| 22 | 2026-11-16 | Aurora Gate | Euphoric Techno | 128 BPM; male/female duet + choir | https://www.youtube.com/watch?v=a6mA32FEMII | https://www.youtube.com/shorts/cujKSJfGNxk (45 s) | version 1 (3:59; v2 `0dd0a305` 3:59): https://suno.com/song/97c52ac0-f64c-455c-b00b-b11e0bc24737 |
| 23 | 2026-11-17 | Desert Djinn | Ethnic Techno | 125 BPM, Arabic Hijaz scale; line "greed or courage?" | https://www.youtube.com/watch?v=QFca4U8GcPE | https://www.youtube.com/shorts/KWzXpNUUKw4 | version 1 (3:59; v2 `7db97cac` 3:56): https://suno.com/song/af960877-3fc5-4dd4-985d-8dec31b8077a |
| 24 | 2026-11-18 (last run of the test) | Earth Mother | Afro Techno | 124 BPM (nudged); udu clay-pot drum, thumb-piano motif, women's choir; theme "we are all one"; natural fade, -14.3 LUFS. Studio first opened on the wrong channel ("Animated Tales 4 All"), a draft landed there and was **permanently deleted**; real upload on Мu Zone. Main video was published before YouTube's content checks finished (watch for any later restriction). No password re-check. | https://www.youtube.com/watch?v=gI3C8L5mVOc | https://www.youtube.com/shorts/JSRYnJFDDEw | version 1 (3:59; v2 `02d3665b` 4:00): https://suno.com/song/b3ba5b04-00ac-4923-9b21-d9e58ef47a17 |

Typical rule applied to choosing a version: both versions are inside 2:30–4:30 → take the one closest to ~3:15; if equal, take the first; verify with ffmpeg (see section 7). Only the chosen one is downloaded (saves allowance).

Suno download allowance trail ("downloads left until Nov 28"): Nov 6: 39 → Nov 7: 37 → Nov 8: 35/36 → Nov 9: 24 → Nov 10: ~22 → Nov 11: ~21 → Nov 12: 18 → Nov 13: ~17 → Nov 15: 12 before / ~11 after → Nov 16: 11 before / ~10 after → Nov 17: 8 before / ~7 after → Nov 18: 5 before / **~4 after**. After the test there is little room for daily releases until the allowance renews on Nov 28.

### Per-playlist live counts

See the table in section 4. Order of "fewest songs live first" was used for picking: after Nov 18 every playlist has 3.

## 6. What's next

1. ~~2026-11-18: Earth Mother, Afro Techno~~ **Done** (published with Short; see release log #24).
2. **After 2026-11-18: do NOT publish.** Pause the automation, collect performance numbers for **all** videos on the channel from YouTube Studio (views, watch time, plus Shorts views, subscribers), summarise them for Farid, and give a recommendation for the next cadence (e.g. fewer songs per week, more Shorts/long mixes, drop weak sub-genres). **No performance data has been collected yet.**
3. Constraint on the recommendation: the shared Suno allowance (~4 downloads until Nov 28) limits new songs.
4. Next unpublished songs per playlist (catalog order), if publishing resumes: High-Tech Minimal → Sand Clock; Melodic → Ocean Within; Peak-Time → Run, Wolf, Run; Japanese → Katana Forge (skipped; see open items) then Bamboo Storm; Dark → Shadow Self; Euphoric → Free Mid-Fall; Ethnic → Sufi Spin (handle respectfully, see master catalog caution); Afro → Rain Dance. If daily releases resume, the rotation continues with **High-Tech Minimal song 4 (Sand Clock)**.
5. Older offers/ideas: 3–4 Shorts per week from released songs; long mix video per playlist at ~8 songs (none of the playlists has 8 yet).

## 7. End-to-end production workflow

Catalog → Suno → download → ffmpeg checks → cover → video → description → YouTube Studio upload → playlist → Short.

1. **Pick the song** from `catalog/` (playlist with fewest live songs; next unpublished; check Release log above).
2. **Research (≤ weekly)**: `research/techno_notes.md` has sub-genre notes (tempo, structure, what viewers praise). Adjust Suno style text, e.g. BPM nudges. No artist names in prompts.
3. **Suno generation**: Create page → paste the song's Lyrics, "Style of Music" box and "Exclude Styles" from `songs/<NN>_<slug>.md` (or the catalog file). **Set the length explicitly:** Create > Advanced > More Options > Duration = Custom (e.g. 4:00; Auto gave 1:59 songs on Nov 10). Suno returns 2 versions.
4. **Pick one version** (duration 2:30–4:30, ideally ~3:15; lyrics/title match; nothing cut off) and note its Suno URL.
5. **Download only that version**: song page → "…" (More options) → Download → dialog with format buttons (M4A, MP3, WAV, MP4, Stems) → click **MP3** → the "Download / Unlock & Download" button may stay grey: **click MP3 a second time**, then click the button once. Do not trigger a second download. Already-unlocked songs re-download for free. Files land in `~/Downloads`. If the button never enables (even after reload), ask Farid to do the download himself.
6. **Audio checks (ffmpeg)**:
   - `ffmpeg -i song.mp3 -af silencedetect=noise=-50dB:d=2 -f null -` → no silence longer than 2 s mid-track (ending silence is fine).
   - `ffmpeg -i song.mp3 -af volumedetect -f null -` and/or `-af ebur128` → reasonable loudness (observed ~ -14 to -15 LUFS).
   - Check the last ~6 s of level for an abrupt cut-off; if it ends abruptly, add a 3–4 s fade-out in the video (`-af afade=t=out:st=<dur-4>:d=4`) instead of spending another download.
   - If it fails, download the other version; if both fail, regenerate once. (The assistant cannot listen to audio; choices are made from duration and measurements.)
7. **Cover (1280×720 PNG)**: one Python/PIL script per song in `scripts/make_cover_*.py` (same base style: dark grid background, glowing motif, Oswald title, accent bar, playlist label, "TECHNO CATALOG" tag; a distinct motif per song). Copy the nearest script and change `slug,title,label,acc` and the motif.
8. **Video**: `ffmpeg -loop 1 -r 2 -i cover.png -i audio.mp3 -t <audio duration in seconds> -c:v libx264 -tune stillimage -pix_fmt yuv420p -c:a aac -b:a 320k -r 2 out.mp4`. **Never use `-shortest`** (it truncated videos). Output is 1280×720 at 2 fps, full audio length. (`scripts/build_videos.sh` is the older batch script from the test batch and *does* use `-shortest -r 1`; it is kept only for reference; do not copy that flag.)
9. **Title and description**: Title pattern `"<Song> | <Playlist genre>"` (example: `Katana | Japanese Techno`). Description = a short hook line + hashtags line, then a multi-paragraph **storytelling description** (the myth/story behind the song, what the vocal says, a "Sound:" paragraph with BPM/key/instruments), "More <genre> in the playlist on this channel.", "Music created with Suno AI. Concept, story and creative direction by the channel owner.", and extra hashtags. Examples: any `songs/*.md` (section "Video description").
10. **YouTube Studio upload** (typical Studio flow; one video per browser step): Create → Upload → select mp4 → title, description → audience "not made for kids" → under "Altered content" choose **Yes** (AI use) → add to the **existing** playlist → visibility **Public** → publish → reload the watch page to verify (public, playlist, description). If Studio asks to "Verify it's you", Farid completes the Google re-verification.
11. **Short (when practical)**: 1080×1920 vertical, **45 s**, taken from the break into drop 2 (or from drop 2). A still frame image (`shorts/NN_frame.png`, 1080×1920) + the audio excerpt via ffmpeg; title like `"Desert Djinn 🏜️ Greed or courage? #techno #shorts"`, description = one hook line + "Full track: <video URL>" + "Music created with Suno AI." + hashtags incl. `#shorts`. Upload as a Short (vertical, < 60 s). The exact Short ffmpeg command was not saved; the files' specs are above (h264/aac, 2 fps, 1080×1920, 45.0 s).
12. **Report to Farid** and update the Release log in this file.

## 8. Known issues and gotchas

- **Suno Download button stays grey (Cloudflare Turnstile).** On Nov 8 and Nov 9 the "Unlock & Download" button never enabled in the assistant's browser (Turnstile check failing silently), so Farid downloaded via handoff. After Farid signed out and back into Suno (Nov 9) the button works: it enables after clicking **MP3 a second time** (verified on a free re-download of Silk Road, then used successfully from Nov 10 to Nov 17; on Nov 13 the MP3 button even enabled on the first click).
- **Suno Duration "Auto" gives ~1:59 songs.** Set **Custom length** under Create > Advanced > More Options (4:00 gives ~3:59). From Nov 10 on, every generation used Custom 4:00.
- **Studio Google password re-verification** ("Verify it's you") appears often; the assistant can't enter the password; Farid must do it (the shared browser was handed over for that). Nothing is stored in this repo.
- **Suno allowance is shared with the Kids Songs Studio bot**, so counts fall faster than own downloads (e.g. 21 → 18 on Nov 12 after one download). ~4 left on Nov 18; renews Nov 28.
- **ffmpeg: never use `-shortest`** with the still-image loop: use `-t <duration>` instead.
- Suno may emit versions over 4:30 (e.g. 4:49 on Nov 12) — that's out of range; take the other version.
- The assistant cannot listen to audio. Quality control is by duration + ffmpeg measurements only. No human listening review was done by the assistant.
- The Page for the master catalog was once unreadable (Nov 6), which led to an ad-hoc song (Katana). Everything it contained is now exported in `catalog/`.
- Download-count display and unlock behaviour are Suno UI details that can change; re-verify.
- Japanese words in lyrics are in simple romaji (long vowels doubled, e.g. ryuu, jiyuu) so Suno pronounces them; Farid wanted a native speaker check before release (see open items).

## 9. File index (this repo) and where the binaries live

```
README.md                      short pointer; read HANDOFF.md first
HANDOFF.md                     this file
catalog/MASTER_CATALOG.md      all 66 songs: name, story, voice, status, per-playlist tables, decisions/cautions (from the master Page)
catalog/01..08_*.md            per-playlist lyrics Pages: full lyrics + production brief + Suno style box + Exclude, with Published/Not yet published status per song
songs/NN_<slug>.md             one file per generated/published song (23 files): the exact Suno inputs used (title, lyrics, style, exclude), the YouTube title and storytelling description, Short title/description, build-file locations
scripts/make_cover_*.py        cover generators (PIL) for songs 09–23 (+ make_assets.py for the 01–08 test-batch covers)
scripts/build_videos.sh        old batch builder for the test batch (uses -shortest; don't reuse that flag)
scripts/make_playlist_descriptions.py   generator for playlist descriptions
workflow/DAILY_ROUTINE.md      the daily automation's exact instructions, tool-neutral
workflow/PLAYLIST_DESCRIPTIONS.md       descriptions of the 8 YouTube playlists
research/techno_notes.md       sub-genre research notes (Peak-Time, Dark, Euphoric, Ethnic, High-Tech Minimal, Melodic, Japanese; not yet Afro)
```

**Binaries (NOT in this repo; they live on the assistant's box and are not accessible to another tool):**
- Covers: `/workspace/youtube/NN_<slug>.cover.png` (1280×720). Videos: `/workspace/youtube/NN_<slug>.mp4` (1280×720, 2 fps, AAC 320k). Shorts: `/workspace/youtube/shorts/*_short.mp4` and `*_frame.png`. Audio: `/workspace/youtube/audio/` and `/workspace/suno/15_silk_road/silk_road.mp3`, `/workspace/suno/16_spirit_of_the_lion/spirit_of_the_lion.mp3`. Original Suno downloads: `/home/box/Downloads`.
- Everything is also on YouTube (videos/Shorts) and in Suno's Library (original audio, for songs 14–23 with URLs above). Covers can be regenerated with the scripts (needs Python + Pillow + the Oswald font at `/usr/share/fonts/truetype/sand-box/google/Oswald/Oswald-VariableFont_wght.ttf`; change the path if missing).
- Original Grok Bot Pages (not accessible elsewhere; exported here): master catalog `2b472171-cc5c-4bf4-a7cd-dcee36546acf`; lyrics Pages High-Tech Minimal `d56bcbe7-c0e9-4ba0-8fbd-c0f44d184ecd`, Melodic `f674f280-7b66-422e-9590-a812378024bf`, Peak-Time `e9fdfac7-59f0-4482-a818-efd8e56ccff1`, Japanese `451c9da8-d415-4575-9ecc-b2988d4721e0`, Dark `61e515f0-9cd5-4660-8cfb-59efa490f16f`, Euphoric `464362f1-5af6-49a1-aae5-9a0aac3874d6`, Ethnic `19a35d16-4cb0-4b2e-be60-dd697e86fb68`, Afro `269afaf1-771f-411c-b045-4e397f681f88`.

## 10. Open items and decisions pending

1. **Katana Forge** (Japanese, catalog song 2): skipped on Nov 14 because its story (a blade forged in fire, water and hammer strikes) nearly duplicates the live **Katana**. Decision pending with Farid: **rewrite it with a different angle, or drop it.** The assistant had planned to raise this with him.
2. **Land of Fire story line on the master catalog:** the master Page still says *"Azerbaijan's eternal flames burn inside every one of us."* It should read *"Eternal flames burn inside every one of us. Your inner fire never dies."* (the Ethnic lyrics Page already has the fixed wording, and `catalog/MASTER_CATALOG.md` here still shows the old text). This is a pending cosmetic fix (it supports the "wider Middle East and Central Asia, not only Azerbaijan" rule).
3. **Romaji / native-speaker check** of the Japanese phrases in the Japanese Techno lyrics (Kitae, Tamashii, Ryuu, Jiyuu, etc.).
4. **Title uniqueness check:** search each final title on Spotify and Apple Music to avoid name clashes (several titles were already renamed for this, e.g. Vibration → Tuning Fork, Eclipse → Moon Eats the Sun).
5. **Possibly regenerate Glitch in the System** (it is only ~2:02, much shorter than the 5-minute brief; Suno clip chosen on Oct 31).
6. **Sufi Spin caution:** whirling is sacred; keep respectful or rename (Farid's call). **Afro Techno:** tie chants/instruments to specific traditions (e.g. Yoruba, Zulu), consider real vocalists to avoid a generic "Africa" feel.
7. **Unknown YouTube URLs** for the 8 test-batch videos and Glitch/Wings of Air must be collected from Studio (they were not recorded in any file I could reach).
8. **Performance review** after Nov 18 (see section 6).

## 11. Monetization notes

- YouTube Partner Program, as recorded in earlier research: **1,000 subscribers plus 4,000 watch hours, or 10M Shorts views** (re-verify the exact windows and whether the subscriber minimum also applies to the Shorts route).
- **Stricter rules for new channels from 2027-02-01** (as noted in earlier research; re-verify before relying on it).
- Other considerations noted: AI-generated music needs the AI-use disclosure = Yes (already standard); repetitive/mass-produced content is a YouTube risk, which is why each song has its own story, cover motif and description. Long mixes (≥ ~8 songs per playlist) and Shorts are the main reach levers.
- No monetization is active; the channel's current subscriber/watch-hour numbers were not collected.

## 12. Gaps in this handoff (be aware)

- YouTube URLs, exact dates and Suno URLs for the 8 test-batch songs: **unknown**. Glitch in the System and Wings of Air: publication is **inferred** (not verified), URLs unknown.
- Suno URLs for Grid Down, Katana, Labyrinth Mind: unknown; Suno URLs for songs 14–23 are known (partial 8-char IDs for the unchosen versions).
- YouTube playlist URLs/IDs: unknown.
- No channel statistics (views, watch time, subscribers) were collected.
- The Short-building ffmpeg command wasn't saved (only the resulting specs).
- The test-batch Suno model version and exact settings were not recorded (later songs: Suno v6 with Custom 4:00 duration).

- **Watch out (2026-11-18):** YouTube Studio may open on another channel of the same Google account ("Animated Tales 4 All", used by the Kids Songs Studio bot). Always confirm the channel is **Мu Zone** before uploading.
