from setuptools import setup, Extension
from Cython.Build import cythonize
import os

include_dirs = [os.path.abspath('.')]

ext_modules = [
    Extension(
        name="solution",
        sources=["example.pyx", "Solution.cpp", "Rat.cpp"],
        include_dirs=include_dirs,
        language="c++"
    )
]

setup(
    ext_modules=cythonize(ext_modules)
)
