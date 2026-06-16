# Learn Git

Welcome to my **Learn Git** project space! This directory serves as a dedicated hands-on workspace documenting my journey through the foundational Git and version control curriculum

The goal of this module is to transition from basic file management to mastering professional tracking, branching, merging, and remote repository collaboration using Git via the command line.

## Project Overview

Unlike structured standalone applications, this folder tracks a fluid series of practical exercises, command-line experiments, and state histories. It simulates real-world software engineering workflows by intentionally creating, modifying, fracturing, and repairing code repositories.

### What Was Done & Mastered:
* **Repository Architecture:** Initialized local repositories from scratch (`git init`), configured essential staging areas, and mapped remote upstream connections to GitHub.
* **Granular Commit Tracking:** Mastered the art of crafting clean, logical snapshots using `git add` and `git commit` alongside descriptive, professional commit messaging.
* **Advanced Branching Strategies:** Moved away from working strictly on production code by spinning up isolated feature branches (`git branch`), context-switching (`git checkout`), and tracking code deviations.
* **History Consolidation & Conflict Resolution:** Combined distinct streams of progress back into the primary lineage using `git merge`. This included hands-on practice resolving intentional merge conflicts—manually triaging overlapping file markers (`<<<<<<<`, `=======`, `>>>>>>>`) to keep critical data intact.
* **Remote Synchronization:** Synchronized localized codebases with remote cloud servers using `git push`, `git fetch`, and `git pull`, while resolving fast-forward and divergent history discrepancies.

## Directory Structure

While completing the interactive prompts from the Boot.dev portal, the layout evolved to track specific configuration patterns:

* **`titles.md`** – A core tracking file used across multiple lessons to demonstrate file modifications, staged changes, and lineage splits across parallel branches (such as `update_titles`).
* **`.gitignore` Integration** – Practical implementation of exclusion rules to ensure sensitive parameters, compiler artifacts, and local environments (like `secure/` paths or tracking lists) never accidentally leak into public staging.

## Execution & Workflow

Every file and history log in this directory was generated natively via the Linux terminal (WSL: Ubuntu). The commands practiced here reflect the exact low-level version control operations used day-to-day by professional software engineering teams. 

*This module marks the successful completion of the core version control prerequisites, establishing the infrastructure needed to manage complex multi-repository projects moving forward!*
