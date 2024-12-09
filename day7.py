from typing import List, Union

with open("inputs/day7", "r") as f:
    lines = f.readlines()

total_cal_p1 = 0
total_cal_p2 = 0


def evaluate(
    numbers: List,
    target: int,
    current_idx: int = 1,
    total: Union[int, None] = None,
    operators: set = {"+", "*"},
) -> bool:
    if total is None:
        total = numbers[0]

    if current_idx == len(numbers):
        return total == target

    results = []
    if "+" in operators:
        results.append(
            evaluate(
                numbers,
                target,
                current_idx + 1,
                total + numbers[current_idx],
                operators,
            )
        )
    if "*" in operators:
        results.append(
            evaluate(
                numbers,
                target,
                current_idx + 1,
                total * numbers[current_idx],
                operators,
            )
        )
    if "||" in operators:
        results.append(
            evaluate(
                numbers,
                target,
                current_idx + 1,
                int(str(total) + str(numbers[current_idx])),
                operators,
            )
        )

    return any(results)


for line in lines:
    test_val = int(line.split(":")[0].strip())
    numbers = list(map(int, line.split(":")[1].strip().split()))

    if evaluate(numbers, test_val, operators={"+", "*"}):
        total_cal_p1 += test_val

    if evaluate(numbers, test_val, operators={"+", "*", "||"}):
        total_cal_p2 += test_val

print(f"Lösung Part 1: {total_cal_p1}\nLösung Part 2: {total_cal_p2}")
