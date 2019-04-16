# Script to execute batch git update commands for given directory and question number

import os
import sys

if len(sys.argv) != 4:
    print("Usage: python update.py [-u or -m] [directory_name] [question_number]")
    sys.exit(1)

program_name = sys.argv[0]
arguments = sys.argv[1:]

mode = arguments[0]
directory_name = arguments[1]
question_number = arguments[2]

def update_github():
    git_add = f"git add {directory_name}/{question_number}"
    os.system(git_add)
    git_commit = f'git commit -m "Added {question_number}"'
    os.system(git_commit)
    os.system('git push')

def make_dir():
   os.system(f'mkdir {directory_name}/{question_number}')
   os.system(f'touch {directory_name}/{question_number}/question.md')
   os.system(f'touch {directory_name}/{question_number}/answer.md')


if mode == '-u':
    update_github()
elif mode == '-m':
    make_dir()
else:
    print("Usage: python update.py [-u or -m] [directory_name] [question_number]")
    sys.exit(1)
