class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p1 = 0
        result = []

        while p1 < len(nums) - 2:
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                p1 += 1
                continue
            p2 = p1 + 1
            p3 = len(nums) - 1

            while p2 < p3:
                total = nums[p1] + nums[p2] + nums[p3]
                if total < 0:
                    p2 += 1
                elif total > 0:
                    p3 -= 1
                else:
                    result.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    p3 -= 1

                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1
                    while p2 < p3 and nums[p3] == nums[p3 + 1]:
                        p3 -= 1
            p1 += 1
        return result
            