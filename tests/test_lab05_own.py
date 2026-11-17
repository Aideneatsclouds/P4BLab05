"""Custom tests for Lab 5 modules: sequence_utils and normalize."""

import pytest
from src.sequence_utils import clean_sequence, is_valid_dna, find_motif
from src.normalize import proportions, cpm


def test_clean_sequence_and_valid_dna_with_n():
    """Test cleaning messy input and validating DNA with 'N' allowed."""
    raw = "  atg cgt n actg \n 123 "
    cleaned = clean_sequence(raw)
    assert cleaned == "ATGCGTNACTG" 
    assert is_valid_dna("ATCGN", allow_n=True) is True
    assert is_valid_dna("ATCGN", allow_n=False) is False


def test_find_motif_overlapping():
    """Test find_motif correctly handles overlapping matches and case insensitivity."""
    assert find_motif("atatat", "at") == [0, 2, 4]
    assert find_motif("AAAA", "AA") == [0, 1, 2]
    assert find_motif("ACGT", "GGG") == []


def test_proportions_input_unchanged():
    """Test that proportions calculates correct fractions and leaves input list completely unchanged."""
    raw_counts = [50, 30, 20]
    original_copy = list(raw_counts)
    
    result = proportions(raw_counts)
    
    assert result == [0.5, 0.3, 0.2]
    assert raw_counts == original_copy, "Input list was mutated by proportions!"


def test_normalize_zero_total_raises_value_error():
    """Test that zero total counts raise a ValueError in proportions and cpm."""
    with pytest.raises(ValueError):
        proportions([0, 0, 0])
        
    with pytest.raises(ValueError):
        cpm([10, 20], library_size=0)