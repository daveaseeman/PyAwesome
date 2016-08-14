from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'a',
  ext_modules = cythonize("a.pyx"),
)