from array import array

nums = array('i', [])
for _ in range(5):
    num = int(input("Enter a  number: "))
    nums.append(num)

nums = sorted(nums)
nums.reverse()
print(nums)

