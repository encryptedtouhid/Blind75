from typing import List

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)

def twoSum(nums: List[int], target: int) -> List[int]:
    
    totalItem = len(nums)
    for num in range(totalItem):
         for rnum in range(num+1, totalItem):
                if(nums[num] + nums[rnum] == target):
                    return [num, rnum]
    
if __name__ == "__main__":
    main()