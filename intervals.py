def inclusive_total(start: int, stop: int) -> int:
    """Return the sum of all integers from start through stop, inclusive."""
    if start > stop:
        raise ValueError("start must not exceed stop")
    return sum(range(start, stop))
