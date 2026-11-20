class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count=0
        while students and count<len(students):
            if students[0]==sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                count=0
            else:
                x=students.pop(0)
                students.append(x)
                count+=1
        return len(students)
        