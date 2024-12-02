with open("inputs/day2", "r") as f:
    lines = f.readlines()

safe_p1 = 0
safe_p2 = 0


def test_safe(nums):
    diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    return (
        True
        if all(1 <= diff <= 3 for diff in diffs)
        or all(-3 <= diff <= -1 for diff in diffs)
        else False
    )


for line in lines:
    nums = [int(num) for num in line.split()]

    if test_safe(nums):
        safe_p1 += 1
        safe_p2 += 1
        continue

    # Part 2
    for i in range(len(nums)):
        modified_report = nums[:i] + nums[i + 1 :]  # Remove one level

        if test_safe(modified_report):
            safe_p2 += 1
            break

print(f"Lösung Part 1: {safe_p1}\nLösung Part 2: {safe_p2}")
