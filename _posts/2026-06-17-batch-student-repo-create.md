---
layout: post
title: A Script to Batch-Create GitHub Repos for My Students
tags: [teaching]
---

GitHub Classroom is being sunset. If you taught with it, you already know; if you didn't, the short version is that the tool a lot of us used to hand every student their own repo for an assignment is going away.

There are alternatives. I'm sure some of them are great, but I'm teaching a class right now, I have a stack of other things due, and "evaluate and learn a new platform" is not a project I'm starting in the middle of the summer quarter. I was banking on GH Classrooms': take a roster, and for each student create a private repo from a template and give that student push access to it. 

Since that isn't available anymore I wrote a script.

A caveat before the code: I'm on Windows. I know. I'm sorry. I need it for qualitative research tools like MaxQDA that don't play nicely anywhere else, and once your machine is your machine you stop relitigating it. The upside is the script runs in Git Bash, which means it's plain bash and works the same way it would on a Mac or a Linux box. You just have to run it in the right shell.

## What It Does

The script reads a CSV roster. For each row it does two things: creates a private repo named `<assignment>-<lastname>` inside a GitHub org I made for the class, generated from a template repo, and then adds that student's GitHub username as a collaborator with push access.

That's the whole job. It leans entirely on the [GitHub CLI](https://cli.github.com/) (`gh`), so as long as you've run `gh auth login` and you have rights to create repos in the org, it just works.

```bash
#!/bin/bash
set -euo pipefail

ORG="your-org-name"
TEMPLATE="hw0"
ASSIGNMENT="hw0"
ROSTER="students.csv"

while IFS=',' read -r username lastname; do
  # skip blank lines
  [ -z "$username" ] && continue

  # sanitize lastname: lowercase, strip whitespace
  lastname=$(echo "$lastname" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
  REPO_NAME="${ASSIGNMENT}-${lastname}"

  echo "Creating ${ORG}/${REPO_NAME} for ${username}..."

  if gh repo view "${ORG}/${REPO_NAME}" >/dev/null 2>&1; then
    echo "  -> repo already exists, skipping creation"
  else
    gh repo create "${ORG}/${REPO_NAME}" \
      --template "${ORG}/${TEMPLATE}" \
      --private
    sleep 1
  fi

  gh api \
    --method PUT \
    "repos/${ORG}/${REPO_NAME}/collaborators/${username}" \
    -f permission=push >/dev/null

  echo "  -> added ${username} as collaborator"

done < "$ROSTER"

echo "All done."
```

Set the four variables at the top: your org name, the template repo, the assignment prefix (which becomes the front half of every repo name), and the path to your roster. That's the only configuration there is.

## The CSV It Expects

The script wants a headerless CSV with two columns: the student's GitHub username, then their last name.

```
geordilf,La Forge
datasoong,Soong
wcrusher,Crusher
sun_hater, Antilles
muppetofman, Solo
```

Username comes first because that's what GitHub needs to add the collaborator. The last name is only used to build the repo name, and the script lowercases it and strips whitespace before doing so, so `La Forge` becomes `laforge` and you get `hw0-laforge`. No header row, and blank lines are skipped.

A wrinkle worth knowing: the repo name is the last name, but the collaborator is the username. If two students share a last name you'll get a collision, so you'd want to disambiguate the name column (add an initial) in that case.

## Running It

Because it's bash, run it in **Git Bash**, not cmd or PowerShell. Open Git Bash, change into the folder, and run it:

```bash
cd "/c/Users/you/path/to/generate-repos"
./generate-repos.sh
```

If it complains about permissions, either `chmod +x generate-repos.sh` first or just call `bash generate-repos.sh`.

Two Windows-specific things bit me, both fixed in the version above. Git Bash rewrites a leading slash in an argument into a Windows path, so `gh api /repos/...` becomes `gh api C:/Program Files/Git/repos/...` and fails; dropping the leading slash fixes it. And `gh api` prints the full JSON invitation object on success, which buries your output in noise, so I send it to `/dev/null`.

The script is also safe to re-run. It checks whether a repo exists before creating it and skips if so, and re-adding a collaborator who's already added is a no-op. So if a run dies halfway, you just run it again instead of untangling what already happened.
