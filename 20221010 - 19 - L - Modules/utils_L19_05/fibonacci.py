def create(args):
    result = [0, 1]
    for i in range(args - 2):
        result.append(result[-1] + result[-2])

    return result


def locate(arg, nums):
    if arg in nums:
        for i in range(len(nums)):
            if arg == nums[i]:
                return i
    else:
        return -1
