def generate_permutations(nums):
    result = []
    
    def backtrack(path, available):
        if not available:
            result.append(path)
            return

        for i in range(len(available)):
            backtrack(path + [available[i]], available[:i] + available[i+1:])
    
    backtrack([], nums)
    return result

nums = [1, 2, 3]
permutations1 = generate_permutations(nums)
for perm in permutations1:
    print(perm)
