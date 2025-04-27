"""
Meeting Rooms
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
"""

from __future__ import annotations
from typing import List, Optional


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True


intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

solution = Interval(0, 0)
print(solution.canAttendMeetings(intervals))
