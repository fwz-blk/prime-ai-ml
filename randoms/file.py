import matplotlib.pyplot as plt

city_pos = {
    "hyd": (3, 4),
    "warangal": (3, 1),
    "nalgonda": (2, 2),
    "tirupati": (4, 3),
    "vijaywada": (5, 2),
    "kadapa": (5, 5),
    "nellore": (2, 3),
    "kurnool": (4, 4)
}

connections = {
    ("hyd", "nalgonda"),
    ("hyd", "warangal"),
    ("hyd", "kurnool"),
    ("nalgonda", "vijaywada"),
    ("kurnool", "kadapa"),
    ("kadapa", "tirupati")
}

plt.figure(figsize=(12, 8))

# Draw connections
for c1, c2 in connections:
    x1, y1 = city_pos[c1]
    x2, y2 = city_pos[c2]

    plt.plot([x1, x2], [y1, y2])

# Draw cities and labels
for city, (x, y) in city_pos.items():
    plt.scatter(x, y)
    plt.text(x, y, city)

# Path
path = ["hyd", "nalgonda", "vijaywada"]

# Highlight path
for i in range(len(path) - 1):
    c1 = path[i]
    c2 = path[i + 1]

    x1, y1 = city_pos[c1]
    x2, y2 = city_pos[c2]

    plt.plot([x1, x2], [y1, y2], linewidth=3)

for i in range(path-1)

plt.savefig("city_graph.png")
