# Day 042 — Git Branching

## Questions & Answers

**What is a Git branch?**
A separate line of development used to work on features independently.

**Why use branches?**
To keep unfinished changes away from the stable `main` branch.

**How do you create a branch?**
```bash
git switch -c feature-name
```

**How do you switch branches?**
```bash
git switch branch-name
```

**How do you merge a branch?**
```bash
git switch main
git merge feature-name
```

**How do you delete a branch?**
```bash
git branch -d feature-name
```

**What is the typical workflow?**
Create a branch → develop → commit → test → merge into `main`.