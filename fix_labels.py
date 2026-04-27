import os

folders = [
    "dataset/labels/train",
    "dataset/labels/val"
]

for folder in folders:
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        with open(path, "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            parts = line.split()

            # skip invalid labels
            if len(parts) < 5:
                continue

            # force class id = 0
            parts[0] = "0"

            new_lines.append(" ".join(parts) + "\n")

        with open(path, "w") as f:
            f.writelines(new_lines)

print("All labels converted to class 0")