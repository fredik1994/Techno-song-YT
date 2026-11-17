# Techno song project: handoff repo

Handoff package for Farid Mammadov's techno catalog (66 songs, 8 playlists, made in Suno and published on the YouTube channel "Мu Zone"). It lets another AI tool or person take over without access to the original assistant, chat, Pages or computer.

**Read [`HANDOFF.md`](HANDOFF.md) first.** It has the goals, Farid's standing rules, the release log, the production workflow, known issues, open decisions and a file index.

- `catalog/`: master catalog + per-playlist lyrics and production briefs (with published status)
- `songs/`: the exact Suno inputs and YouTube texts for each of the 23 songs made so far
- `workflow/`: the daily release routine (tool-neutral) and playlist descriptions
- `research/`: techno sub-genre research notes
- `scripts/`: cover and video helper scripts

No credentials, tokens, e-mails or phone numbers are stored here. Audio, video and image files are intentionally not included.
