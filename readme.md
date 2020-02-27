# Adversarial Search
CSCI 404 Project 2  
(This file is saved as .txt to comply with the project requirements but is written in Markdown. It can be previewed with https://markdownlivepreview.com/ for an easier lecture)

## 1. Names and CWID
David An 10727498
Leo Chely 10818125

## 2. Programming Language
Python 3.X (no compiler)

## 3. Code Structure
We used the starting code for the basic operations. We added a tree generator function using the anytree library, an evaluator to generate the scores of the leaves of the generated tree. This score is based on the actual scores and on the most important heuristic desribed in the research paper given in the project description. We also added and an alpha-beta pruning depth limited algorithm to find the best next move for the AI. Finding the next move may take a larger amount of time when running with large depths. However, the AI gives an almost immediate result for a depth value lower than 7.

## 4. How to run
First, run `pip install -r requirements.txt`. This will install the dependencies for the tree. Then use the command `python3 maxconnect4.py interactive  [input_file] [computer-next/human-next] [depth]` or the command `python3 maxcconnect4.py one-move [input_file] [output_file] [depth]`. `python3` should be replaced by `python` if you run the program on the school computers (or if your system only has python3 installed).
