from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'filter',
  ext_modules = cythonize("filter_cpython.py"),
)

# python3 setup2.py build_ext --inplace