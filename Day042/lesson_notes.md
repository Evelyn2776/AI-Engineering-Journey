# Day 042 — Git Branching

## What I Learned

A Git branch is a separate line of development. It allows me to work on a new feature without directly changing the stable `main` branch.
For example, I can create a feature branch, make changes, test them, and later merge the changes into `main`.

### Important Commands
```bash
git branch
```
Shows the branches in the repository.

```bash
git switch -c feature-name
```
Creates a new branch and switches to it.

```bash
git switch main
```
Switches back to the `main` branch.

```bash
git merge feature-name
```
Combines the feature branch changes into the current branch.

```bash
git branch -d feature-name
```
Deletes a merged branch.

### Basic Workflow
```text
Create Branch → Work → Commit → Test → Merge → Delete
```

## Key Takeaway
Branches make it safer to develop features and experiment without breaking the stable project.
