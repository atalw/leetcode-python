# Script to execute batch git update commands for given directory and question number

import os
import sys

if len(sys.argv) != 3:
    print("Usage: python update.py [directory_name] [question_number]")
    sys.exit(1)

program_name = sys.argv[0]
arguments = sys.argv[1:]

directory_name = arguments[0]
question_number = arguments[1]

def update_github():
    git_add = f"git add {directory_name}/{question_number}"
    os.system(git_add)
    git_commit = f'git commit -m "Added {question_number}"'
    os.system(git_commit)
    os.system('git push')


update_github()
