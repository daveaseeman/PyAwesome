from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'filter2',
  ext_modules = cythonize("filter_cpython3.pyx"),
)

# python3 setup2.py build_ext --inplace