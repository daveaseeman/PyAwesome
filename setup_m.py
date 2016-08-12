from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Mandel',
  ext_modules = cythonize("mandel.pyx"),
)