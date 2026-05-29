---
name: job-search-tracker
description: >
  Use this skill whenever the user wants to log contacts, opportunities, or notes into their job search tracker spreadsheet. Triggers include: pasting raw notes from a call, conference, or conversation; mentioning someone they met; describing an org or role to watch; saying things like "add this to my tracker", "log this contact", "log to tracker", "I met someone", "update my sheet", or sharing messy notes with names, emails, affiliations, or orgs. Also triggers when the user says "set up my tracker" or "set up the job search skill" — this means they are a first-time user and need the Setup flow. Always use this skill rather than asking the user to reformat their notes — the skill's job is to do that work for them. Output is either a personalized SKILL.md file (Setup) or clean CSV rows (Update).
---

# Job Search Tracker Skill

A two-mode skill for job seekers who want to turn messy notes into structured Google Sheet rows without reformatting anything themselves.

**Mode 1 — Setup:** First-time user. Run the interview, then generate a personalized SKILL.md file they install to replace this one.
**Mode 2 — Update:** Returning user whose personalized skill is active. Parse raw notes and output CSV rows.

---

## Step 0 — Which mode?

Read the conversation carefully.

- User says "set up my tracker" or similar first-time language → **Mode 1 (Setup)**
- User pastes notes, names, orgs, or conference info and wants to log them → **Mode 2 (Update)**
- Unclear → ask: *"Have you set up your personalized tracker skill yet, or is this your first time?"*

---

## MODE 1 — Setup

Tell the user:

> "Let's set up your tracker. I'll ask a few questions in two rounds — answer as briefly or fully as you like. At the end I'll generate a personalized skill file you install once, and from then on you won't need to explain your context again."

### Round 1 — About you and your search
Ask all of these together:

1. What's your name (how you sign emails)?
2. What field or role are you searching in? (e.g. "CS PhD looking for policy and industry research roles")
3. What's your rough timeline? (e.g. "graduating spring 2027")
4. Any location preferences or constraints?
5. Anything you're explicitly *not* looking for? (e.g. "no startups", "no R1 faculty positions")

Wait for their answers. Then ask Round 2.

### Round 2 — Context and tracker setup
6. What's your current work or research focus in a sentence or two? (Helps infer relevance when logging contacts)
7. Any conferences, communities, or programs you're active in? (Helps recognize shorthand in your notes — e.g. "met at PETS" or "from my cohort")
8. What tracks are you searching across? (default: Industry / Policy / Academic — confirm or customize)
9. Do you want the standard column schema, or do you have custom columns?

Show them the defaults and let them adjust:

**Default Contacts columns:** Name | Affiliation | Track | Relationship | How I Know Them | Last Outreach | What Happened | Next Move | Due Date

**Default Opportunities columns:** Role / Org | Type | Track | Deadline | Status | Materials Package | Source / URL | Next Action | Due Date | Notes

### After both rounds — generate the personalized skill

Write a complete, self-contained SKILL.md file (see template below) and present it inside a code block. Tell the user:

> "Here's your personalized skill file. To install it:
> 1. Go to Settings → Customize → Skills in Claude
> 2. Install this as a new skill (name it something like `my-job-tracker`)
> 3. You can uninstall this setup skill if you want — your personalized one replaces it
>
> Once installed, just say **'log to tracker'** and paste your notes. If it doesn't trigger automatically, say **'use my-job-tracker skill'** to invoke it explicitly."

---

### Personalized skill template

Generate this with the user's answers filled in. Keep it complete and self-contained — the user should never need to refer back to this skill again.

```markdown
---
name: [their chosen skill name, e.g. my-job-tracker]
description: >
  Use this skill when [NAME] wants to log contacts, opportunities, or notes into their job search tracker. Triggers on: "log to tracker", "add to my sheet", "I met someone", pasting raw notes from calls or conferences, mentioning a new person or org. Output is CSV rows ready to paste into Google Sheets.
---

# [NAME]'s Job Search Tracker

## About [NAME]
- **Sign-off name:** [name]
- **Search focus:** [field and role types]
- **Timeline:** [graduation or availability]
- **Location:** [preferences]
- **Not looking for:** [exclusions]
- **Current work:** [research or role description]
- **Active communities:** [conferences, programs, networks — so shorthand like "met at X" is recognized]

## Tracker schema
**Tracks:** [Industry / Policy / Academic / custom list]

### Contacts columns (in order)
[pipe-separated column names]

### Opportunities columns (in order)
[pipe-separated column names]

## Standard materials packages
- Fellowship (policy): Resume (Policy) + Cover Letter (Policy) + Writing Sample + Essays
- Full-time role (policy): Resume (Policy) + Cover Letter (Policy) + Writing Sample
- Full-time role (industry): Resume (Industry) + Cover Letter (Industry)
- Postdoc / Academic: CV + Cover Letter + Research Statement + Writing Sample + 3 Refs
- Org to Watch: TBD — monitor for openings
[adjust based on what the user told you]

## Your job
Take [NAME]'s raw notes — however messy — and produce clean CSV rows for their tracker. Never ask them to reformat. Extract what's there, infer what you can, flag what's missing.

### Processing rules
1. Read everything before outputting — understand the full picture first
2. Identify each item: person (→ Contacts), org/role (→ Opportunities), or both
3. Infer track, relationship strength, and next move from context
4. Produce rows even with missing info — use [TBD] placeholders, flag gaps at the end
5. Next moves must be specific: "Email to ask for intro to her children's privacy colleague" not "Follow up"
6. Due dates: Hot = 1 week / Warm = 2–3 weeks / Cold = 4–6 weeks — adjust if notes give a specific timeframe

### Relationship strength
- **Cold** — knows of them, no real exchange
- **Warm** — had a real conversation (conference, call, email)
- **Hot** — explicitly offered to help, or strong ongoing connection

## CSV output rules
- One CSV block per tab (Contacts and/or Opportunities)
- Every field in double quotes — no exceptions, including empty fields ("")
- No commas inside field values — rephrase using "and" or a dash
- Each entry is exactly one line — never wrap across lines
- Source / URL field: URL only. Put "Via [name]" in Notes, not in the URL field
- Column count check: count commas outside quotes — must equal number of columns minus 1. Fix any row that fails.

## Output format

CONTACTS TAB
"[col1]","[col2]",...
"[value]","[value]",...

OPPORTUNITIES TAB
"[col1]","[col2]",...
"[value]","[value]",...

Flags
- [urgent follow-up]
- [missing info to track down]
- [anything ambiguous]

No preamble. No explanation. CSV then flags.
```

---

## MODE 2 — Update

This mode runs when the user's **personalized skill** is active. The personalized skill is self-contained — it has the user's schema, context, and all processing rules built in. Follow its instructions directly.

If somehow Mode 2 is reached without a personalized skill active, prompt the user to run setup first.