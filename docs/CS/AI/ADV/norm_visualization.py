import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_cube_grid(ax, size, highlighted_slice=None, is_batch_norm=True):
    """Create a cube with grid lines and optional highlighted slice."""
    vertices_base = np.array([
        [0,0,0], [1,0,0], [1,1,0], [0,1,0],
        [0,0,1], [1,0,1], [1,1,1], [0,1,1]
    ])
    
    faces = [
        [0,1,2,3], [4,5,6,7], [0,1,5,4],
        [2,3,7,6], [0,3,7,4], [1,2,6,5]
    ]

    for i in range(size[0]):
        for j in range(size[1]):
            for k in range(size[2]):
                vertices = vertices_base + [i,j,k]
                
                is_highlighted = (k == highlighted_slice) if is_batch_norm else (j == highlighted_slice)
                
                color = ('royalblue' if is_batch_norm else 'orange') if is_highlighted else 'white'
                alpha = 0.6 if is_highlighted else 0.1
                
                poly3d = Poly3DCollection([vertices[faces[f]] for f in range(6)], 
                                        alpha=alpha, facecolor=color, edgecolor='black', linewidth=0.5)
                ax.add_collection3d(poly3d)

# Create figure with two subplots
fig = plt.figure(figsize=(15, 7))

# Batch Norm subplot
ax1 = fig.add_subplot(121, projection='3d')
create_cube_grid(ax1, (6,6,6), highlighted_slice=4, is_batch_norm=True)
ax1.set_title('Batch Norm', pad=20, fontsize=14)

# Layer Norm subplot  
ax2 = fig.add_subplot(122, projection='3d')
create_cube_grid(ax2, (6,6,6), highlighted_slice=2, is_batch_norm=False)
ax2.set_title('Layer Norm', pad=20, fontsize=14)

# Configure both subplots
for ax in [ax1, ax2]:
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([]) 
    ax.set_zticks([])
    ax.view_init(elev=15, azim=225)
    ax.set_box_aspect([1,1,1])

plt.tight_layout()
plt.savefig('norm_visualization.jpg', dpi=600, bbox_inches='tight')