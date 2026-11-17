"""Week 5 extension - side-effect-free normalisation functions."""


def proportions(counts: list[float]) -> list[float]:
    """Return each count divided by the total; the input is not changed.

    Raises:
        ValueError: if the total is zero (a list of zeros would look like data).
    """
    if not counts:
        raise ValueError("Counts list cannot be empty.")

    total = sum(counts)
    if total == 0:
        raise ValueError("Total sum of counts cannot be zero.")

    return [x / total for x in counts]


def cpm(counts: list[float], library_size: float | None = None) -> list[float]:
    """Counts per million; library_size defaults to the sum of counts.

    Raises:
        ValueError: if library_size is zero or negative, or if counts is empty.
    """
    if not counts:
        raise ValueError("Counts list cannot be empty.")

    if library_size is None:
        library_size = sum(counts)

    if library_size <= 0:
        raise ValueError("Library size must be greater than zero.")

    return [(x / library_size) * 1_000_000 for x in counts]
