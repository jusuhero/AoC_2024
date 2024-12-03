import re

with open("inputs/day3", "r") as f:
    lines = f.read()

pattern1 = r"mul\((\d+),(\d+)\)"
pattern2 = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
matches1 = re.findall(pattern1, lines)
matches2 = re.finditer(pattern2, lines)

enabled = True
loesung_p2 = 0
for match in matches2:
    if match.group().startswith("mul"):
        if enabled:
            # Extract the numbers and calculate the product
            x, y = map(int, match.groups())
            loesung_p2 += x * y
    elif match.group() == "do()":
        enabled = True  # Enable processing
    elif match.group() == "don't()":
        enabled = False


loesung_p1 = sum(int(x) * int(y) for x, y in matches1)

print(f"Lösung Part 1: {loesung_p1}\nLösung Part 2: {loesung_p2}")
