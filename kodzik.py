
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Kosmiczna scena
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
fig.patch.set_facecolor("#050515")
ax.set_facecolor("#050515")

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

ax.set_axis_off()

# Gwiazdy
np.random.seed(42)
stars = np.random.uniform(-5, 5, (180, 3))

ax.scatter(
    stars[:, 0],
    stars[:, 1],
    stars[:, 2],
    color="white",
    s=np.random.uniform(1, 8, 180),
    alpha=0.8
)

# Wierzchołki kostki masła
vertices = np.array([
    [-1, -0.7, -0.6],
    [ 1, -0.7, -0.6],
    [ 1,  0.7, -0.6],
    [-1,  0.7, -0.6],
    [-1, -0.7,  0.6],
    [ 1, -0.7,  0.6],
    [ 1,  0.7,  0.6],
    [-1,  0.7,  0.6]
])

faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [2, 3, 7, 6],
    [0, 3, 7, 4],
    [1, 2, 6, 5]
]

colors = [
    "#FFD84A",
    "#FFE878",
    "#F5C52E",
    "#FFE45C",
    "#EAB52C",
    "#FFDA55"
]

cube = Poly3DCollection(
    [[vertices[i] for i in face] for face in faces],
    facecolors=colors,
    edgecolors="#FFF0A0",
    linewidths=1.5
)

ax.add_collection3d(cube)

# Animacja
def update(frame):
    angle = frame * 0.035

    # Obrót kostki
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

    Ry = np.array([
        [np.cos(angle * 0.7), 0, np.sin(angle * 0.7)],
        [0, 1, 0],
        [-np.sin(angle * 0.7), 0, np.cos(angle * 0.7)]
    ])

    Rz = np.array([
        [np.cos(angle * 0.5), -np.sin(angle * 0.5), 0],
        [np.sin(angle * 0.5), np.cos(angle * 0.5), 0],
        [0, 0, 1]
    ])

    rotation = Rz @ Ry @ Rx

    # Ruch kostki w przestrzeni
    x = 1.5 * np.sin(frame * 0.025)
    y = 1.2 * np.cos(frame * 0.018)
    z = 0.8 * np.sin(frame * 0.04)

    rotated = vertices @ rotation.T
    rotated += np.array([x, y, z])

    new_faces = [
        [rotated[i] for i in face]
        for face in faces
    ]

    cube.set_verts(new_faces)

    return cube,

ani = FuncAnimation(
    fig,
    update,
    frames=1000,
    interval=30,
    blit=False
)

plt.title(
    "🧈 BUTTER IN SPACE 🚀",
    color="gold",
    fontsize=18,
    pad=20
)

plt.show()
