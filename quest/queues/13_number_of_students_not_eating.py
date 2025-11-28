"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

    If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i-th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j-th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""
from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """

        tried = 0
        while students:
            if students[0] == sandwiches[0]:
                # pop(0) in a list is O(n)
                students.pop(0)
                sandwiches.pop(0)
                tried = 0
            else:
                s = students.pop(0)
                students.append(s)
                tried += 1
        
            if tried == len(students):
                break
        
        return len(students)

    def queueCountStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """

        st_q = deque()
        for s in students:
            st_q.append(s)

        tried = 0
        students_left = len(st_q)
        while st_q:
            if st_q[0] == sandwiches[0]:
                # popleft() in a dequeue is O(1)
                st_q.popleft()
                sandwiches.pop(0)
                tried = 0
                students_left -= 1
            else:
                s = st_q.popleft()
                st_q.append(s)
                tried += 1

            if tried == students_left:
                break

        return students_left
