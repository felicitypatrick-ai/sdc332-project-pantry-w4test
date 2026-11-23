"""Northside Food Pantry: waitlist for full days."""


def waitlist_position(waitlist, family):
    """Return the family's place in line, or 0 when not on the waitlist."""
    if family not in waitlist:
        return 0
    return waitlist.index(family) + 1
