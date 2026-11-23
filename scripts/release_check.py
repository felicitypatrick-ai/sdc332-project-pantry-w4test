"""Release check: run after each deploy with the deployed folder (course starter app)."""
import os
import sys

release, environment = sys.argv[1], sys.argv[2]
sys.path.insert(0, release)  # import the deployed files, not the repository's

from settings import SATURDAY_CAPACITY
from slots import slots_left
from waitlist import waitlist_position

print(f"Release check: {environment}")
print(open(os.path.join(release, "BUILD_INFO.txt")).read().strip())
print("Saturday capacity (families):", SATURDAY_CAPACITY)
print("Open pickup slots with 18 booked:", slots_left(SATURDAY_CAPACITY, 18))
print("Place in line of the first on the waitlist:", waitlist_position(["Garcia", "Nguyen"], "Garcia"))
print("Release check finished.")
