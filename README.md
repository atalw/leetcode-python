# Leetcode Python Solutions

This repository contains the python solutions to Leetcode problems covering all difficulty levels. It also contains an automation script I wrote to speed up management of this repo. Read more [here](#update.py).

## File Structure

```
.
+-- difficulty mode
|   +-- question number
```

## update.py

A script to automate file structure creation and github sync.

### Usage
`$ python update.py [mode] [difficulty] [question_number]`

Example:

`python update -m easy 70`

### 2 modes

 - `-m`: (make_dir) Make a new dir as specified and create question.md and answer.md inside
 - `-u`: (update_github) batch execute github commands to push to remote

### Difficulty

Leetcode has 3 difficulty modes:

 - Easy
 - Medium
 - Hard
