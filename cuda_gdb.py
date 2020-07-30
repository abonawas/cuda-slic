from survos2.improc.regions.slic import slic3d

from skimage import data, color, filters
from skimage import img_as_float32

def test_slic3d_grayscale_runs():
    blob = data.binary_blobs(length=50, n_dim=3, seed=2)
    blob = img_as_float32(blob)
    labels = slic3d(blob, n_segments=100, compactness=3)

test_slic3d_grayscale_runs()