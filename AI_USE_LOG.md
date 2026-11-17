# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 5
- Student name: YAASWINY ABBIRAMAVALLY THINAHARAN
- Matric no: A24CS0213
- Group ID: <group work only, else n/a>
- AI level: 1
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [X] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 2026-11-10 14:00
- Tool: Google Gemini, Version 2026, Accessed Nov 2026, https://gemini.google.com
- Purpose: explain
- Prompt: "let's do task 1"
- Output: Suggested using regular expressions for `clean_sequence`, set comparison for `is_valid_dna`, and length-based calculations for `gc_content`.
- Verified by: Ran pytest (`python -m pytest`)
- My change: Accepted the logic, corrected a lowercase typo (`false` to `False`), and integrated the functions.
- Used in: `src/sequence_utils.py` (`clean_sequence`, `is_valid_dna`, `gc_content`)

## Entry 2

- Date: 2026-11-10 14:15
- Tool: Google Gemini, Version 2026, Accessed Nov 2026, https://gemini.google.com
- Purpose: generate-code
- Prompt: "how to implement reverse_complement and find_motif"
- Output: Provided code snippets using `str.maketrans` with slicing for reverse complement and a sliding window for motif matching.
- Verified by: Ran pytest (`python -m pytest`)
- My change: Adapted the translation table to handle `N` bases and ensured case-insensitive matching for motifs.
- Used in: `src/sequence_utils.py` (`reverse_complement`, `find_motif`)

## Entry 3

- Date: 2026-11-10 14:30
- Tool: Google Gemini, Version 2026, Accessed Nov 2026, https://gemini.google.com
- Purpose: generate-code
- Prompt: "let's go task 3"
- Output: Provided side-effect-free implementations for `proportions` and `cpm` using list comprehensions and value error checks.
- Verified by: Ran pytest (`python -m pytest`)
- My change: Accepted the code directly since it avoids in-place list mutations and handles zero/negative divisions cleanly.
- Used in: `src/normalize.py` (`proportions`, `cpm`)

## Entry 4

- Date: 2026-11-10 14:45
- Tool: Google Gemini, Version 2026, Accessed Nov 2026, https://gemini.google.com
- Purpose: review
- Prompt: "Task 4. Module quality: docstrings, type hints, no side effects"
- Output: Reviewed requirements for docstrings, type hints, mutable defaults avoidance, and print-free function design.
- Verified by: Ran `ruff check src` and `ruff format src`
- My change: Verified that type hints, docstrings, and guards (`if __name__ == "__main__":`) were properly structured across both modules.
- Used in: `src/sequence_utils.py` and `src/normalize.py`

## Entry 5

- Date: 2026-11-10 15:00
- Tool: Google Gemini, Version 2026, Accessed Nov 2026, https://gemini.google.com
- Purpose: tests-plan
- Prompt: "let's go task 5"
- Output: Provided a test template covering both modules, an immutability check on input lists, and zero-total error tests.
- Verified by: Ran `python -m pytest` (collecting all 9 test items)
- My change: Updated the expected assertion for `clean_sequence` to correctly account for lowercase letters (`'n'`) being preserved, then accepted the rest.
- Used in: `tests/test_lab05_own.py`

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->
