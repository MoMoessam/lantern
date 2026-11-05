##E1:
```
origin	https://github.com/MoMoessam/lantern (fetch)
origin	https://github.com/MoMoessam/lantern (push)
```

##E2:
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   notes.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.txt

diff --git a/notes.txt b/notes.txt
index c00740e..96d6463 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1,3 +1,4 @@
 placeholder
 typo
 another one
+dsfg
diff --git a/notes.txt b/notes.txt
index 96d6463..6394d47 100644
--- a/notes.txt
+++ b/notes.txt
@@ -2,3 +2,4 @@ placeholder
 typo
 another one
 dsfg
+another change
```

##E4:
```
*   a9ec1d9 Merge branch 'fix/strip-title'
|\  
| * 9957c21 fix(tasks): strip whitespace from title
* | 0c8989b feat(tasks):add done flag to tasks
|/  
* 9c5356f refactor(notes): rename draft.txt to notes.txt
* 6de128a chore(placeholder): add draft.txt
* c000ed2 feat(lantern.py): add argparse entry point
* 7ecf083 feat(tasks): add add_task and list_tasks
*   7250306 Merge branch 'feature/pretty-json'
|\  
| * d90da24 Format JSON output with indentation
* | 4774f05 Write JSON keys in sorted order
|/  
* 016927f Remove scratch placeholder file
* 60387b0 add scratch.txt
*   f54090b Merge branch 'main' of https://github.com/MoMoessam/lantern
|\  
| * 9e50698 Fix table formatting in README.md
| * b9204ec Add Mohamed Essam to the team list in README
* | 7f1e12d add usage documentation and storage functionality
|/  
* b576882 add team member to Readme.md
* a6993da Initial commit
```

##E5:
```
-(a) is at HEAD@{8,7}

e58af5e HEAD@{0}: commit: test commit to check rule
dafa788 HEAD@{1}: reset: moving to HEAD@{3}
634e188 HEAD@{2}: reset: moving to HEAD~1
dafa788 HEAD@{3}: reset: moving to HEAD@{1}
634e188 HEAD@{4}: reset: moving to HEAD~1
dafa788 HEAD@{5}: commit: docs(notes.txt): added another line to notes.txt
634e188 HEAD@{6}: pull --no-rebase: Merge made by the 'ort' strategy.
f2fa040 HEAD@{7}: commit (amend): docs(typo): added line to notes.txt
0781df4 HEAD@{8}: commit: chore(typo): added typo to notes.txt
8c8c5b2 HEAD@{9}: commit: fix(gitignore): untrack .env and ignore it
a50fe56 HEAD@{10}: commit: chore(env): add local variables
a9ec1d9 HEAD@{11}: commit (merge): Merge branch 'fix/strip-title'
0c8989b HEAD@{12}: merge feature/done-flag: Fast-forward
9c5356f HEAD@{13}: checkout: moving from feature/done-flag to main
0c8989b HEAD@{14}: commit: feat(tasks):add done flag to tasks
9c5356f HEAD@{15}: checkout: moving from fix/strip-title to feature/done-flag
9957c21 HEAD@{16}: commit: fix(tasks): strip whitespace from title
9c5356f HEAD@{17}: checkout: moving from main to fix/strip-title
9c5356f HEAD@{18}: checkout: moving from feature/done-flag to main
016927f HEAD@{19}: checkout: moving from main to feature/done-flag
9c5356f HEAD@{20}: checkout: moving from fix/strip-title to main
9c5356f HEAD@{21}: checkout: moving from main to fix/strip-title
9c5356f HEAD@{22}: pull: Fast-forward
c000ed2 HEAD@{23}: reset: moving to c000ed2
6de128a HEAD@{24}: reset: moving to 6de128a
9c5356f HEAD@{25}: commit: refactor(notes): rename draft.txt to notes.txt
6de128a HEAD@{26}: commit: chore(placeholder): add draft.txt
c000ed2 HEAD@{27}: commit: feat(lantern.py): add argparse entry point
7ecf083 HEAD@{28}: commit: feat(tasks): add add_task and list_tasks
7250306 HEAD@{29}: clone: from https://github.com/MoMoessam/lantern
```
```
-(c)
e58af5e HEAD@{0}: commit: test commit to check rule
dafa788 HEAD@{1}: reset: moving to HEAD@{3}
634e188 HEAD@{2}: reset: moving to HEAD~1
dafa788 HEAD@{3}: reset: moving to HEAD@{1}
634e188 HEAD@{4}: reset: moving to HEAD~1
dafa788 HEAD@{5}: commit: docs(notes.txt): added another line to notes.txt
634e188 HEAD@{6}: pull --no-rebase: Merge made by the 'ort' strategy.
f2fa040 HEAD@{7}: commit (amend): docs(typo): added line to notes.txt
0781df4 HEAD@{8}: commit: chore(typo): added typo to notes.txt
8c8c5b2 HEAD@{9}: commit: fix(gitignore): untrack .env and ignore it
a50fe56 HEAD@{10}: commit: chore(env): add local variables
a9ec1d9 HEAD@{11}: commit (merge): Merge branch 'fix/strip-title'
0c8989b HEAD@{12}: merge feature/done-flag: Fast-forward
9c5356f HEAD@{13}: checkout: moving from feature/done-flag to main
0c8989b HEAD@{14}: commit: feat(tasks):add done flag to tasks
9c5356f HEAD@{15}: checkout: moving from fix/strip-title to feature/done-flag
9957c21 HEAD@{16}: commit: fix(tasks): strip whitespace from title
9c5356f HEAD@{17}: checkout: moving from main to fix/strip-title
9c5356f HEAD@{18}: checkout: moving from feature/done-flag to main
016927f HEAD@{19}: checkout: moving from main to feature/done-flag
9c5356f HEAD@{20}: checkout: moving from fix/strip-title to main
9c5356f HEAD@{21}: checkout: moving from main to fix/strip-title
9c5356f HEAD@{22}: pull: Fast-forward
c000ed2 HEAD@{23}: reset: moving to c000ed2
6de128a HEAD@{24}: reset: moving to 6de128a
9c5356f HEAD@{25}: commit: refactor(notes): rename draft.txt to notes.txt
6de128a HEAD@{26}: commit: chore(placeholder): add draft.txt
c000ed2 HEAD@{27}: commit: feat(lantern.py): add argparse entry point
7ecf083 HEAD@{28}: commit: feat(tasks): add add_task and list_tasks
7250306 HEAD@{29}: clone: from https://github.com/MoMoessam/lantern
```

##E7:
```
remote: error: GH006: Protected branch update failed for refs/heads/main.        
remote: 
remote: - Changes must be made through a pull request.        
To https://github.com/MoMoessam/lantern
 ! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'https://github.com/MoMoessam/lantern'

```