# cuda-slic: A CUDA implementation of the SLIC Superpixel algorithm

## SLIC
SLIC stands for __simple linear iterative clustering__. SLIC uses
tiled k-means clustering to segment an input image into a set
of superpixels/supervoxels.

This library was designed to segment large 3D images coming from different
detectors at the [Diamond Light Source](https://diamond.ac.uk). These images
can be up to 500 GB so using a serial CPU code is out of the question.

To speed up processing we use GPU acceleration to achieve great speed
improvements over alternative implementations. `cuda-slic` borrows its API
from `skimage.segmentation.slic`.

## Install
```bash
pip install cuda-slic
```
`cuda-slic` uses the pycuda which has the following non-python
build dependencies:
1. gcc and g++/gcc-c++ on Linux.

and the following runtime dependencies:
1. gcc and g++/gcc-c++ on Linux.
2. the cudatoolkit for linking with cuda libraries.
3. the nvcc compiler. Ships with newer cudatoolkit versions.

See the [pycuda docs](https://wiki.tiker.net/PyCuda/Installation/) for 
installation instructions.

## Usage
```python
from cuda_slic import slic
from skimage import data

# 2D RGB image
img = data.astronaut() 
labels = slic(img, n_segments=100, compactness=10)

# 3D gray scale
vol = data.binary_blobs(length=50, n_dim=3, seed=2)
labels = slic(vol, n_segments=100, multichannel=False, compactness=0.1)

# 3D multi-channel
# volume with dimentions (z, y, x, c)
# or video with dimentions (t, y, x, c)
vol = data.binary_blobs(length=33, n_dim=4, seed=2)
labels = slic(vol, n_segments=100, multichannel=True, compactness=1)
```

# Development
##### Prerequisites:
1. gcc and g++/gcc-c++ installed and available on PATH.
2. cudatoolkit installed and CUDA_HOME pointing to its location.
3. `nvcc` compiler. Ships with recent versions of cudatoolkit.

## Dependency Management

We use `conda` as a dependency installer and virtual env manager.
A development environment can be created with
```bash
conda env create -f environment.yml
```
now you can activate the virtual env with `conda activate cuda-slic`,
and deactivate with `conda deactivate`.
To add a dependency, add it to the [environment.yml](environment.yml) file, then you can run
```bash
conda env update -f environment.yml
```
to keep `environment.yml` file as lean as possible, development dependencies
are kept in `requirements_dev.txt` and can be installed with
```bash
conda install --file requirements_dev.txt -c conda-forge
```
or
```bash
pip install -r requirements_dev.txt
```

## Tests
In the [notebooks](notebooks) folder there are Jupyter notebooks
where the segmentation algorithm can be visually inspected.

Our unit-testing framework of choice is [Py.test](https://docs.pytest.org/en/latest/).
The unit-tests can be run with
```bash
conda activate cuda-slic
pip install pytest
pytest
```
or
```bash
conda activate cuda-slic
pip install tox
tox
```