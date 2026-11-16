"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    raise NotImplementedError("TODO: implement clean_sequence")


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    raise NotImplementedError("TODO: implement is_valid_dna")


def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    raise NotImplementedError("TODO: implement gc_content")


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    raise NotImplementedError("TODO: implement reverse_complement")


def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    raise NotImplementedError("TODO: implement find_motif")
