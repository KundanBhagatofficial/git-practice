"""Tiny module used only by the Bounty Workstation controlled canary."""


def increment(value: int) -> int:
    """Return the integer immediately after ``value``."""
    # Intentional canary defect: the controlled bounty must fix this to value + 1.
    return value
