import numpy as np

def save_as_ply(filename, points):
    assert points.ndim == 2
    assert points.shape[1] == 6
    header = """ply
        format ascii 1.0
        element vertex {0}
        property float x
        property float y
        property float z
        property uchar red
        property uchar green
        property uchar blue
        element face 0
        property list uchar int vertex_indices\r\nend_header"""
    number_of_points = points.shape[0]
    with open(filename, "w") as ply_file:
        ply_file.write(header.format(number_of_points) + '\n')
        point_format = ("%.18f", "%.18f", "%.18f", "%d", "%d", "%d")
        np.savetxt(ply_file, points, delimiter=" ", fmt=point_format)
