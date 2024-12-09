with open("inputs/day5", "r") as f:
    rules, updates = f.read().split("\n\n")

# rules = [
#     tuple(map(int, line.split("|"))) for line in lines.split("\n\n")[0].splitlines()
# ]
# checknums = [line.split(",") for line in lines.split("\n\n")[1].splitlines()]
rules = rules.split("\n")
updates = [x.strip().split(",") for x in updates.split("\n")]
updates.pop()


def sort_by_rules(nums):
    def prio(x):
        return -sum(f"{x}|{y}" in rules for y in nums)

    return sorted(nums, key=prio)


matches = []
not_matches = []

for nums in updates:
    sorted_nums = sort_by_rules(nums)
    middle = int(sorted_nums[len(nums) // 2])
    if sorted_nums == nums:
        matches.append(middle)
    else:
        not_matches.append(middle)

print(f"Lösung Part 1: {sum(matches)}\nLösung Part 2: {sum(not_matches)}")
