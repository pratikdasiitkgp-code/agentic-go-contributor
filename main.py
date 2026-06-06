from git import Repo

from agents.issue_analyzer import *
from agents.repo_search import *
from agents.context_builder import *
from agents.planner import *
from agents.code_generator import *
from agents.validator import *
from agents.pr_generator import *

issue_url = input(
    "Enter GitHub Issue URL: "
)

issue = extract_issue(
    issue_url
)

import os

repo_path = "repositories/cobra"

if not os.path.isdir(repo_path):
    Repo.clone_from(
        "https://github.com/spf13/cobra.git",
        repo_path
    )
else:
    print("Repository already exists.")

go_files = get_go_files(
    "repositories/cobra"
)

index, chunks, file_names = \
    build_context(go_files)

context = search_context(
    issue["description"],
    index,
    chunks,
    file_names
)

plan = create_plan(issue)

print(plan)

patch = generate_patch(
    issue,
    context
)

with open(
    "outputs/patch.diff",
    "w",
    encoding="utf-8"
) as f:
    f.write(patch)

test_result = run_tests()

print(test_result)

pr = generate_pr(
    issue,
    patch
)

with open(
    "outputs/pr.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(pr)

print("Done")