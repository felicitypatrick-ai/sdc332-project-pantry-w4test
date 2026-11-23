"""Northside Food Pantry: open pickup slots."""


def slots_left(capacity, booked):
    """Return how many pickup slots are still open."""
    return max(capacity - booked, 0)


def can_book(capacity, booked, party_size=1):
    """Return True when the booking fits in the open pickup slots."""
    return party_size <= slots_left(capacity, booked)
