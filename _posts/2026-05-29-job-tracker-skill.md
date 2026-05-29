# I Built a Claude Skill to Log My Job Search Notes So I Don't Have To

I am on the job market. Not right now — I finish my PhD in 2027 — but soon enough that I needed to start building the spreadsheet that everyone says you need and nobody actually maintains past month two.

You know the one. A tab for opportunities. A tab for contacts. Columns for deadlines and statuses and next actions and the name of the person you met at that conference whose card you definitely did not lose. A system that works great the day you build it and slowly dies as the friction of keeping it updated accumulates.

The friction point for me was the gap between how I take notes and what the spreadsheet wants. After a call or a conference I have a block of text. Messy, abbreviated, first-name-only. The spreadsheet wants structured rows. Converting one to the other isn't hard, but it's just annoying enough that I kept putting it off, and putting it off is how systems die.

So I built a Claude skill to close that gap.

## What the Skill Does

The skill takes raw notes, exactly as I'd write them after a call or a conference, and outputs clean CSV rows ready to paste into Google Sheets.

Something like this goes in[^1]:

```
Geordi La Forge
- Starfleet
- Met at conference, he's on the fellows selection committee
- Said to reach out before submitting the application
- geordi+data4ever@starfleet.org
```

And something like this comes out:

```
CONTACTS TAB
"Name","Affiliation","Track","Relationship","How I Know Them","Last Outreach","What Happened","Next Move","Due Date"
"Geordi La Forge","Starfleet","Policy","Hot","Met at conference. Email: geordi+data4ever@starfleet.org","May 2026","On Fellows selection committee — said to reach out before submitting application","Email before submitting fellowship app","Sep 15 2026"
```

One paste. Split by comma in Google Sheets (Data → Split text to columns). Done.

It also handles opportunities — if my notes mention an org or a role worth watching, it generates a row for the Opportunities tab at the same time, with a URL, a materials package, and a next action. It flags anything missing at the end without making me feel bad about it.

## The Design Problem I Had to Solve

The skill works well because it knows context I'd otherwise have to re-explain every time: what kind of roles I'm looking for, what my research is about, what the column schema of my tracker is, how to infer whether someone is a warm or cold contact.

The obvious approach is to hard-code all of that into the skill file. Which is what I did for myself. But I wanted to share this publicly, and I didn't want to share my personal job search context with everyone.

The other obvious approach is a config file the user pastes into every conversation — which works but is friction, and friction is exactly what I was trying to eliminate.

The solution I landed on is a two-mode skill that generates a second, personalized skill.

**Mode 1: Setup.** First time you use the skill, it interviews you. Two rounds of questions: who you are and what you're looking for, then what your tracker schema looks like. At the end, it generates a complete personalized `SKILL.md` tailored to your search; i.e., your name, your tracks, your column schema, your communities. You install that as a new skill.

**Mode 2: Update.** Your personalized skill is now active. You paste raw notes, say "*log to tracker*," and get CSV rows back. No config to paste, no context to re-explain. The skill already knows everything it needs.

The personalized skill is self-contained. It lives in your Claude settings like any other skill. You can edit it directly if your situation changes. (e.g., changed your timeline, added a new track, switched your column schema.) It travels with you across conversations because it's installed, not pasted.

## How to Invoke It

Once you've installed the setup skill, just say **"set up my tracker"** and it starts the interview.

Once your personalized skill is installed, say **"log to tracker"** and paste your notes. Skills in claude.ai trigger from natural language. The phrase is unambiguous enough to fire reliably without any special syntax.

If the skill doesn't trigger automatically (this can happen if you have many skills installed and descriptions compete for attention), you can invoke it explicitly by name: **"use my-job-tracker skill"** or whatever you named it during setup. That's the explicit invocation method in claude.ai. No slash commands needed, just the skill's name in plain English.

## What I Actually Learned Building This

Most of it was obvious in retrospect.

The hardest part was writing the personalized skill template so it would work correctly when Claude fills it in. A template full of placeholders is easy to write. A template that, once filled in, produces consistent well-formed CSV across arbitrary messy input — that took more iteration. The key was including explicit output rules and a column-count check directly in the generated skill, not just in the setup instructions.

## One Note on Slash Commands

If you use Claude Code (the terminal tool), skills there can be invoked with `/skill-name` syntax. These are explicit slash commands like you'd use in Slack. That's a Claude Code feature, not the browser interface. In claude.ai, the invocation is natural language. I mention this because it's a common point of confusion when I was telling my friends about the skill.

## The Skill

Download the skill file below and install it in Claude via Settings → Customize → Skills.[^2]

**[Download job-search-tracker.md](/assets/files/job-search-tracker-v3.md)**

To get started, install the skill and say: *"Set up my tracker."* Claude will run the interview, generate your personalized skill file, and tell you exactly how to install it. After that, you won't need this one anymore.

[^1]: Why yes, this is the same style of toy example I used for my guide to applying for a PhD. Thank you for noticing. 
[^2]: Claude Skills are a feature of claude.ai that let you give Claude persistent instructions and context for specific tasks. A skill is a markdown file with a name, a description that controls when it triggers, and instructions in the body. You install it once and it's available across all your conversations.
