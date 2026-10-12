# Author: Ozan Inan
# Source: Programming for the Puzzled -- Srini Devadas
# Problem: You Will All Conform
#
# Given a list of cap orientations ('F' = forward, 'B' = backward),
# find the minimum number of group flip commands to make everyone uniform.
# Two approaches are implemented:
#   1. pleaseConformOpt  - two-pass: finds intervals first, then decides which to flip
#   2. pleaseConformOnePass - single-pass: uses the majority property to flip on the fly


# ---------------------------------------------------------------------------
# Sample inputs
# ---------------------------------------------------------------------------
caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
caps_empty = []


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def print_flip_command(start: int, end: int) -> None:
    """Print a human-readable flip instruction for positions start..end."""
    if start == end:
        print(f"Person in position {start}, please flip your cap!")
    else:
        print(f"People in positions {start} through {end}, flip your caps!")


# ---------------------------------------------------------------------------
# Algorithm 1 – Two-pass interval approach
# ---------------------------------------------------------------------------
def pleaseConformOpt(caps: list) -> None:
    """Print the minimum flip commands using a two-pass interval strategy.

    Pass 1: Walk the list and record contiguous same-direction intervals,
            counting how many forward (F) and backward (B) intervals exist.
    Pass 2: Flip whichever orientation has *fewer* intervals — that is the
            cheaper target and guarantees the fewest group commands.

    Args:
        caps: List of 'F' / 'B' strings representing cap orientations.
    """
    if not caps:
        print("No one is in the stadium — nothing to do!")
        return

    # --- Pass 1: build interval list ---
    forward_count = 0
    backward_count = 0
    intervals = []  # each entry: (start_idx, end_idx, orientation)
    start = 0

    # Iterate from index 1; when the direction changes, close the current interval
    for i in range(1, len(caps)):
        if caps[i] != caps[start]:
            intervals.append((start, i - 1, caps[start]))
            if caps[start] == 'F':
                forward_count += 1
            else:
                backward_count += 1
            start = i

    # Close the final interval (no sentinel needed)
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward_count += 1
    else:
        backward_count += 1

    # --- Pass 2: flip the minority orientation ---
    # If counts are equal we default to flipping 'B'; both choices are optimal.
    flip_target = 'F' if forward_count < backward_count else 'B'

    for start_idx, end_idx, orientation in intervals:
        if orientation == flip_target:
            print_flip_command(start_idx, end_idx)


# ---------------------------------------------------------------------------
# Algorithm 2 – Single-pass approach
# ---------------------------------------------------------------------------
def pleaseConformOnePass(caps: list) -> None:
    """Print the minimum flip commands in a single pass (no stored intervals).

    Key insight: In any alternating sequence, the orientation of caps[0]
    appears in at least as many intervals as the opposite orientation.
    So always flipping the opposite of caps[0] achieves the minimum with
    no look-ahead and no extra memory proportional to n.

    Args:
        caps: List of 'F' / 'B' strings representing cap orientations.
    """
    if not caps:
        print("Empty list — no one is at the stadium!")
        return

    majority = caps[0]          # orientation we keep; the other gets flipped
    flip_target = 'B' if majority == 'F' else 'F'
    flip_start = None           # start of the current flip interval (or None)

    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] == flip_target:
                # Entering a segment that needs flipping
                flip_start = i
            else:
                # Leaving a flip segment — emit the command
                print_flip_command(flip_start, i - 1)
                flip_start = None

    # Handle a flip segment that runs all the way to the last element
    if caps[-1] == flip_target:
        print_flip_command(flip_start, len(caps) - 1)


# ---------------------------------------------------------------------------
# Demo / quick tests
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    print("=== Opt (two-pass) on caps ===")
    pleaseConformOpt(caps)

    print("\n=== OnePass on caps ===")
    pleaseConformOnePass(caps)

    print("\n=== OnePass on caps_empty ===")
    pleaseConformOnePass(caps_empty)
    print(f"Length of caps_empty: {len(caps_empty)}")

