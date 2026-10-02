def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {num: index for index, num in enumerate(nums)}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in hashmap and hashmap[complement] != index:
            return [index, hashmap[complement]]

    return []

print(two_sum([1, 1, 2, 2, 3], 2))
