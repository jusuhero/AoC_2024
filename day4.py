with open("inputs/day4", "r") as f:
    lines = f.readlines()

text = [list(line.strip()) for line in lines]
rows = len(text)
cols = len(text[0])
matches = []
search_word = "XMAS"
directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (-1, 0),  # Up
    (1, 0),  # Down
    (1, 1),  # diagonal down right
    (-1, -1),  # diagonal up left
    (1, -1),  # diagonal down left
    (-1, 1),  # diagonal down right
]

for y in range(rows):
    for x in range(cols):
        for direction in directions:
            dx, dy = direction
            match = True
            for step in range(len(search_word)):
                nx, ny = x + step * dx, y + step * dy

                # out of bounds is bad
                if not (0 <= nx < cols and 0 <= ny < rows):
                    match = False
                    break

                # if not the word, also bad
                if text[ny][nx] != search_word[step]:
                    match = False
                    continue

            if match:
                matches.append(((x, y), direction))

print(f"Lösung Part 1: {len(matches)}")
