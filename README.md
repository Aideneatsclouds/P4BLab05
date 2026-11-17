# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: YAASWINY ABBIRAMAVALLY THINAHARAN A24CS0213

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
`proportions()` raises a `ValueError` when the total sum of counts is zero to prevent division by zero and avoid returning a misleading list of zeros that could masquerade as valid expression data. The input list remains completely untouched because the function computes and returns a brand-new list using a list comprehension (`[x / total for x in counts]`) instead of performing any in-place assignments.
