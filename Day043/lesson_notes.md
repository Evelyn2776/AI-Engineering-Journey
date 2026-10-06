# Day 043 — GitHub & Remote Repositories

## What I Learned

A remote repository is a copy of a Git repository stored online, usually on GitHub. It allows me to back up, share, and collaborate on my projects.

### Important Commands
```bash
git remote -v
```
Shows the remote repositories connected to the local repository.

```bash
git push
```
Sends local commits to GitHub.

```bash
git pull
```
Gets changes from the remote repository.

```bash
git clone <repository-url>
```
Creates a local copy of a remote repository.

### Local vs Remote
```text
Local Repository ←→ GitHub
       Git push  →
       ← Git pull
```

## Key Takeaway
Git manages version history, while GitHub provides a remote place to store and share Git repositories.
