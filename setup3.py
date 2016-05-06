from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
  name = 'filter2',
  ext_modules = cythonize("filter_cpython3.pyx"),
  include_dirs=[numpy.get_include()],
  define_macros=[('CYTHON_TRACE', '1')]
)

# python3 setup2.py build_ext --inplace