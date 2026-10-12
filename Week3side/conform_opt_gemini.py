"""Conform Optimization Module.

Based on 'Programming for the Puzzled' by Srini Devadas (Chapter 2: You Will All Conform).

Given an array of baseball cap orientations ('F' for forward, 'B' for backward),
this module determines the minimum number of group commands required to get all
caps facing the same direction.
"""

from typing import List, Tuple

FORWARD = "F"
BACKWARD = "B"


def format_flip_command(start: int, end: int) -> str:
    """Format a human-readable instruction to flip caps for an interval.

    Args:
        start: Starting index (0-based) of the interval.
        end: Ending index (0-based, inclusive) of the interval.

    Returns:
        Formatted instruction string.
    """
    if start == end:
        return f"Person in position {start}, please flip your cap!"
    return f"People in positions {start} through {end}, flip your caps!"


def find_intervals(caps: List[str]) -> List[Tuple[int, int, str]]:
    """Partition the cap list into contiguous intervals of identical orientation.

    Args:
        caps: List of cap orientations ('F' or 'B').

    Returns:
        List of tuples representing (start_index, end_index, orientation).
    """
    if not caps:
        return []

    intervals: List[Tuple[int, int, str]] = []
    start = 0

    for i in range(1, len(caps)):
        if caps[i] != caps[start]:
            intervals.append((start, i - 1, caps[start]))
            start = i
    intervals.append((start, len(caps) - 1, caps[start]))

    return intervals


def please_conform_opt(caps: List[str]) -> List[str]:
    """Calculate and print minimum flip commands using a two-pass interval strategy.

    First pass: Identify all intervals and count frequencies of 'F' vs 'B' intervals.
    Second pass: Output instructions for the orientation that has fewer intervals.

    Args:
        caps: List of cap orientations ('F' or 'B').

    Returns:
        List of generated command strings.
    """
    if not caps:
        print("Empty cap list provided; no flips needed.")
        return []

    intervals = find_intervals(caps)

    # Count occurrences of intervals for each orientation
    forward_intervals = sum(1 for _, _, orientation in intervals if orientation == FORWARD)
    backward_intervals = len(intervals) - forward_intervals

    # If all caps already face the same direction, no flips needed
    if forward_intervals == 0 or backward_intervals == 0:
        print("All caps are already facing the same direction!")
        return []

    # Choose the orientation with fewer intervals to minimize commands
    target_flip = FORWARD if forward_intervals < backward_intervals else BACKWARD

    commands: List[str] = []
    for start, end, orientation in intervals:
        if orientation == target_flip:
            cmd = format_flip_command(start, end)
            commands.append(cmd)
            print(cmd)

    return commands


def please_conform_one_pass(caps: List[str]) -> List[str]:
    """Calculate and print minimum flip commands in a single pass without storing intervals.

    Algorithmic insight:
    In any alternating sequence of intervals, the orientation of caps[0] appears
    at least as many times as the opposite orientation. Therefore, flipping intervals
    that do NOT match caps[0] is guaranteed to achieve the theoretical minimum flips
    without needing a second pass or extra memory.

    Args:
        caps: List of cap orientations ('F' or 'B').

    Returns:
        List of generated command strings.
    """
    if not caps:
        print("Empty cap list provided; no flips needed.")
        return []

    commands: List[str] = []
    start = 0
    target_to_flip = BACKWARD if caps[0] == FORWARD else FORWARD

    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] == target_to_flip:
                # Started a new interval that needs to be flipped
                start = i
            else:
                # Just finished an interval that needed to be flipped
                cmd = format_flip_command(start, i - 1)
                commands.append(cmd)
                print(cmd)

    # Handle the trailing interval if it ended at the last element
    if caps[-1] == target_to_flip:
        cmd = format_flip_command(start, len(caps) - 1)
        commands.append(cmd)
        print(cmd)

    return commands


# Backward compatibility aliases for legacy function names
pleaseConformOpt = please_conform_opt
pleaseConformOnepass = please_conform_one_pass


def main() -> None:
    """Run demonstration test cases."""
    sample_caps_1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    sample_caps_2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    empty_caps: List[str] = []

    print("=== Two-Pass Algorithm (sample_caps_1) ===")
    please_conform_opt(sample_caps_1)

    print("\n=== One-Pass Algorithm (sample_caps_1) ===")
    please_conform_one_pass(sample_caps_1)

    print("\n=== Edge Case: Empty List ===")
    please_conform_one_pass(empty_caps)


if __name__ == "__main__":
    main()

