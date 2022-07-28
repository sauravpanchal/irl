# number-of-students-doing-homework-at-a-given-time

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([queryTime >= start and queryTime <= end for start, end in zip(startTime, endTime)])