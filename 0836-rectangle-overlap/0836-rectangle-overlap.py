class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:

        if rec2[0] >= rec1[2]:   # rec2 is right of rec1
            return False

        if rec2[2] <= rec1[0]:   # rec2 is left of rec1
            return False

        if rec2[1] >= rec1[3]:   # rec2 is above rec1
            return False

        if rec2[3] <= rec1[1]:   # rec2 is below rec1
            return False

        return True


#  '''
#  class Solution:
#     def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
#         return not (
#             rec2[0] >= rec1[2] or
#             rec2[2] <= rec1[0] or
#             rec2[1] >= rec1[3] or
#             rec2[3] <= rec1[1]
#         )
#         '''
