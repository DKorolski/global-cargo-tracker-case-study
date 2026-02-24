# Transfer to New Public Repo (Safe Workflow)

This document describes a safe way to move the local draft into a separate public repository without risking accidental publication of private files.

## Recommended Approach

Use a brand new local directory for the public repo and copy only the curated draft files.

Do **not** add the public repo as a second remote to the private repository.

## Step-by-Step

Assumption:

- private repo path: `.../global-cargo-tracker`
- public draft exists in: `.../global-cargo-tracker/public-case-study-draft/`
- target public repo folder (new): `.../global-cargo-tracker-case-study/`

### 1. Create a New Local Folder (sibling directory)

```bash
cd ..
mkdir -p global-cargo-tracker-case-study
```

### 2. Copy Only the Draft Files

```bash
cp -R global-cargo-tracker/public-case-study-draft/. global-cargo-tracker-case-study/
```

### 3. Initialize the New Git Repository

```bash
cd global-cargo-tracker-case-study
git init
git branch -M main
```

### 4. Add Minimal Repo Metadata (if not added yet)

Suggested files:

- `.gitignore`
- `LICENSE` (if you want one)

### 5. Run Local Safety Checks

```bash
rg -n "api[_-]?key|token|secret|password|passwd|Authorization|AIza|X-ACCESS-KEY|BEGIN PRIVATE KEY" .
python3 demo/demo_cli.py
git status --short
```

### 6. Connect to the Public GitHub Repository

After you create `global-cargo-tracker-case-study` on GitHub:

```bash
git remote add origin <YOUR_PUBLIC_REPO_URL>
git remote -v
```

### 7. Review and Commit

```bash
git add .
git diff --staged
git commit -m "Initial public case study draft"
```

### 8. Push

```bash
git push -u origin main
```

## Optional Next Improvements Before Public Push

1. Add 1-2 redacted screenshots to `assets/screenshots/`
2. Add a short `What I would redesign today` section
3. Add a small CI check for demo execution (later)

## Red Flags (Stop and Recheck)

- You see `db/`, `src/global-cargo-tracker/`, or `src/jupyther/` in `git status`
- You see `.db`, `.sql` dumps, or `.kdbx` files in the new repo
- `git remote -v` points to the private repository

