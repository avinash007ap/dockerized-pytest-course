avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git status
On branch exceptions
Your branch is up to date with 'origin/exceptions'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   scripts/chp2/video3/mapmaker_exceptions_start.py
        modified:   tests/chp2/video3/test_exceptions_start.py

no changes added to commit (use "git add" and/or "git commit -a")
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git add  scripts/chp2/video3/mapmaker_exceptions_start.py  tests/chp2/video3/test_exceptions_start.py
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git commit -m "Assignment done"
[exceptions b726b64] Assignment done
 2 files changed, 9 insertions(+)
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git push --set-upstream origin exceptions
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 2 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 1.18 KiB | 1.18 MiB/s, done.
Total 10 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
To https://github.com/avinash007ap/dockerized-pytest-course
   2abcac5..b726b64  exceptions -> exceptions
branch 'exceptions' set up to track 'origin/exceptions'.
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
@avinash007ap ➜ /workspaces/dockerized-pytest-course (master) $ git checkout -b parameter
Switched to a new branch 'parameter'
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ 