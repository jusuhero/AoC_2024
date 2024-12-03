import re

with open("inputs/day3", "r") as f:
    lines = f.read()

pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
matches = list(re.finditer(pattern, lines))
enabled = True

loesung_p1 = sum(
    int(x) * int(y)
    for match in matches
    if match.group().startswith("mul")
    for x, y in [match.groups()]
)
loesung_p2 = sum(
    int(x) * int(y)
    for match in matches
    if (enabled := match.group() == "do()" or (enabled and match.group() != "don't()"))
    and match.group().startswith("mul")
    for x, y in [match.groups()]
)

print(f"Lösung Part 1: {loesung_p1}\nLösung Part 2: {loesung_p2}")
