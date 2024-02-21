from array import array
from random import randrange

nums1 = []
for _ in range(5):
    nums1.append(randrange(100))

nums2 = array('i', [])
for _ in range(3):
    nums2.append(int(input("Enter a number: ")))


nums = []

for num in nums1:
    nums.append(num)

for num in nums2:
    nums.append(num)

nums = sorted(nums)

for num in nums:
    print(num)
