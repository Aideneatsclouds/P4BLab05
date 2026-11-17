"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


import re

def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    # Keep only alphabetical characters and convert to upper case
    cleaned = re.sub(r'[^A-Za-z]', '', raw)
    return cleaned.upper()


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    if not sequence:
        return False
    
    valid_bases = set("ACGTN") if allow_n else DNA_BASES
    # Ensure all characters in the uppercase sequence are within the valid set
    return set(sequence.upper()) <= valid_bases

def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    if not is_valid_dna(sequence, allow_n=False):
        raise ValueError("Invalid DNA sequence or empty string provided for GC content calculation.")
    
    upper_seq = sequence.upper()
    gc_count = upper_seq.count('G') + upper_seq.count('C')
    return (gc_count / len(upper_seq)) * 100.0


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    raise NotImplementedError("TODO: implement reverse_complement")


def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    raise NotImplementedError("TODO: implement find_motif")
