import git
from git import Repo
import os


if __name__ == "__main__":
    repo_path = os.path.dirname(__file__)
    print(repo_path)

    repo = git.Repo(repo_path)

    commit_sha = repo.head.commit
    tags = repo.tags

    commit_tag = None
    for t in tags:
        if t.commit == commit_sha:
            commit_tag = t
            break

    print(commit_sha)
    print(commit_tag)

