# Workflotics reel automation runbook

Owner: Abyan (hello@workflotics.com). Goal: fully automatic reels to Instagram + LinkedIn via ZapierW (Publer). Abyan only checks occasionally. Never ask him questions, decide and act.

## Rules
- Reply/notes start with "Abyan!", never use em dashes, end messages with a separate "Your next task" section.
- Reels: educational, rotate every service (see topic_queue in state.json), about 1 in 4 promotes Workflotics. 9:16, 15 s max (build asserts 14.9), voice + SFX + soft music, no fade-in, frame 0 is the finished hook, say "ay eye" for AI, end text "Contact us to learn more.", no characters, safe zones respected (builder already does this).
- Caption: hook line, 3 or 4 numbered points, AI automation angle, small task, offer line, "Contact us to learn more.", max 5 hashtags, 1400 to 1600 chars. Style reference: tools/captions-batch1.json.
- Never mention residency. Never mention Reclaivo.
- Do not use auto_comment (Publer free plan refuses it). Tell Abyan he can add first comments manually.
- Save Zapier tasks: about 2 per reel (upload_media + create_post for both accounts together). Never retry a timed-out create_post blindly.

## Cadence
- Until 2 Dec 2026 (Zapier trial): 2 reels/day at 13:00 and 19:00 UTC (= UK in winter; use 12:00/18:00 UTC in BST).
- After: about 6 reels/week (e.g. Mon-Sat 13:00 UTC). Track Zapier task use against about 100/month.
- Keep up to 10 scheduled at once (Publer free limit). Min 1 minute between posts.

## Steps for a refresh run
1. Read state.json. Work out how many slots are free before 10 are queued; count from the last scheduled time forward.
2. `git pull`, then `bash tools/setup.sh` (installs deps, downloads kokoro models, copies builder to /home/claude/reels).
3. For each new reel: add a script to tts.py and a config to build.py (copy an existing reel's pattern and a scene*.js for a new topic), run `python3 build.py rN stills`, `python3 verify.py` to check centring, view a still, then `python3 build.py rN full`. Output /home/claude/reels/rN.mp4. Render several in parallel.
4. Copy mp4s to reels/ in this repo, commit, push to main. Note the commit hash.
5. For each reel: upload_media (upload_type=url, ONE url per call) with https://cdn.jsdelivr.net/gh/reclaivo/workflotics@<commit>/reels/<file>.mp4 (raw GitHub URLs are rejected). Then create_post: state scheduled, workspace_id and account_ids from state.json, media_ids, text = caption, scheduled_at ISO UTC.
6. Update state.json (scheduled list, next_reel_number, topic_queue), commit and push.
7. Create the next scheduled run (create_trigger) about 2 days before the queue empties, pointing at this runbook. Keep runs to twice a week.

## Brand images (owner approved for reels)
Real-photo style images live in brand-images/ (hero, ai-ad-videos, 3d-websites, voice-agents, workflow-automation, property-tours). Use them as backgrounds, cutaways or b-roll in future reels where the topic fits (e.g. voice agents reel uses the voice-agents card, 3D websites reel uses the 3d-websites card). Keep clear empty space top and bottom. Fetch via jsDelivr pinned to a commit like the mp4s.
