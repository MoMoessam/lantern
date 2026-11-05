# Git Workshop Evidence – Person B

**Name:** Somaia Ahmed Fakhreldin

**GitHub Username:** [somaiaahmed](https://github.com/somaiaahmed)

**Repository:** [MoMoessam/lantern](https://github.com/MoMoessam/lantern)

---

## E1 – Clone and Authentication

The following output shows the repository being cloned using SSH authentication:

```text
Cloning into 'lantern'...
The authenticity of host 'github.com (140.82.121.3)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 12 (delta 3), reused 2 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (12/12), done.
Resolving deltas: 100% (3/3), done.
```
Output of ```git remote -v:```

```
origin  git@github.com:MoMoessam/lantern.git (fetch)
origin  git@github.com:MoMoessam/lantern.git (push)
```

**Authentication method:** SSH.


## E3 – Commit and Tree SHA Evidence

Two consecutive commits on `main`:

|               | Latest commit                              | Previous commit                            |
| ------------- | ------------------------------------------ | ------------------------------------------ |
| Commit SHA    | `72503068ac46bfe92986abff00d40ac211204ffe` | `d90da241d17aacfbb3fa81c1d38e44fdb6310a79` |
| Root Tree SHA | `d33dd08603162491fa461a5a02bae18d252072aa` | `197ba9eb5dd033096c9b7b284f9947a7ed4defcb` |

### File object comparison

Identical blob

- Filename: `README.md`
- Blob SHA: `a3052bca9ab7a6d4fe1b24a14fe1086b36c81651`

Another identical file:

- Filename: `docs/usage.md`
- Blob SHA: `c337cdb30a1d7a4f0be344317f29a02f6e3ddcb4`

Different blob

- Filename: `storage.py`
- Latest commit blob SHA: `887318ece7625a1ad5a83dfd99e6623e2b807182`
- Previous commit blob SHA: `0d6f11f65943efe9862ea4497599867e8ead2994`



## E4 – Branching and Merge History

History graph after completing the Requirement 3 merges:

```text
*   7250306 (HEAD -> main, origin/main, origin/HEAD) Merge branch 'feature/pretty-json'
|\
| * d90da24 Format JSON output with indentation
* | 4774f05 Write JSON keys in sorted order
|/
* 016927f Remove scratch placeholder file
```

This demonstrates the two branches, their separate commits, and the merge commit on `main`.

## E5 – Reflog Evidence

### Drill B – Wrong Branch

Commit reference: [8df4e5db75614d2a66460d64452da62c4c3798a8](https://github.com/MoMoessam/lantern/commit/8df4e5db75614d2a66460d64452da62c4c3798a8)

```text
3f4e032 (HEAD -> main, origin/main, origin/HEAD, docs/usage-heading)
HEAD@{0}: merge docs/usage-heading: Fast-forward

e33aab2
HEAD@{1}: reset: moving to origin/main

3f4e032 (HEAD -> main, origin/main, origin/HEAD, docs/usage-heading)
HEAD@{2}: checkout: moving from docs/usage-heading to main

3f4e032 (HEAD -> main, origin/main, origin/HEAD, docs/usage-heading)
HEAD@{3}: checkout: moving from main to docs/usage-heading

3f4e032 (HEAD -> main, origin/main, origin/HEAD, docs/usage-heading)
HEAD@{4}: commit:
```

Original commit: [e33aab2729d858fe612ecf5aae09b5dd8eeaf808](https://github.com/MoMoessam/lantern/commit/e33aab2729d858fe612ecf5aae09b5dd8eeaf808)

```text
781e0e7 (HEAD -> main, origin/main, origin/HEAD)
fix(docs): remove unsupported lantern command

3d4b788
docs(usage): document lantern remove command
```

The original documentation commit remains in history, and a separate corrective commit undoes its change. -->

## E6 – Stash Evidence

Stash listing showing the unfinished sorting work before it was reapplied:

```text
stash@{0}: On feature/list-sort: unfinished list sort option
```

The stash preserved the unfinished `list --sort` changes while the empty-list bug was implemented on a separate branch.

---

## Repository and Contributor Information

| Field | Details |
|---|---|
| Contributor | Somaia Ahmed Fakhreldin |
| Role | Person B |
| GitHub | [somaiaahmed](https://github.com/somaiaahmed) |
| Repository | [MoMoessam/lantern](https://github.com/MoMoessam/lantern) |