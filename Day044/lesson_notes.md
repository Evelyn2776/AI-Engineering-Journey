# Day 044 — GitHub Branches & Pull Requests

## What I Learned
A local branch can be pushed to GitHub as a remote branch. A Pull Request (PR) is used to propose changes from one branch to another, usually `main`.

### Important Commands
```bash
git push -u origin feature-name
```
Pushes a local branch to GitHub and connects it to the remote branch.

```bash
git branch -r
```
Shows remote branches.

```bash
git branch -a
```
Shows local and remote branches.

## Pull Request Workflow
```text
Create Branch → Code → Commit → Push → Pull Request → Review → Merge
```

## Key Takeaway
Pull Requests make it easier to review and safely merge changes into a project's main branch.