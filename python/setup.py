# Copyright (C) 2015-2019 Savoir-faire Linux Inc.
# Author: Guillaume Roguez <guillaume.roguez@savoirfairelinux.com>
# Author: Adrien Béraud <adrien.beraud@savoirfairelinux.com>
#
# A Python3 wrapper to access to OpenDHT API
# This wrapper is written for Cython 0.22
#
# This file is part of OpenDHT Python Wrapper.
#
#    OpenDHT Python Wrapper is free software:  you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    OpenDHT Python Wrapper is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with OpenDHT Python Wrapper. If not, see <https://www.gnu.org/licenses/>.
#

from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(name="opendht",
      version="1.9.4",
      description="Python wrapper for OpenDHT",
      url='https://github.com/savoirfairelinux/opendht',
      author="Adrien Béraud, Guillaume Roguez, Simon Désaulniers",
      license="GPLv3",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Distributed Computing',
          'Topic :: System :: Networking'
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      cmdclass = { 'build_ext' : build_ext },
      ext_modules = cythonize(Extension(
          "opendht",
          ["./opendht.pyx"],
          include_dirs = ['../include'],
          language="c++",
          extra_compile_args=["-std=c++11"],
          extra_link_args=["-std=c++11"],
          libraries=["opendht"],
          library_dirs = ['.', '../src/.libs']
      ))
)