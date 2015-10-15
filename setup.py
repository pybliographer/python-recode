# -*- python -*-

import os
import sys

from distutils.core import setup, Extension, Command
from distutils.errors import DistutilsExecError
from distutils.command.install import install as base_install

version = '1.2.7'


def error(msg):
    sys.stderr.write('setup.py: error: %s\n' % msg)


class run_check (Command):
    """ Run all of the tests for the package using uninstalled (local)
    files """

    description = "Automatically run the test suite for the package."
    user_options = []

    def initialize_options(self):
        self.build_lib = None

    def finalize_options(self):
        # Obtain the build_lib directory from the build command
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        # Ensure the extension is built
        self.run_command('build')

        # test the uninstalled extensions
        libdir = os.path.join(os.getcwd(), self.build_lib)
        sys.path.insert(0, libdir)

        import testsuite

        try:
            failures = testsuite.run()

        except RuntimeError, msg:
            sys.stderr.write('error: %s\n' % msg)
            raise DistutilsExecError('please consult the "Troubleshooting" '
                                     'section in the README file.')

        if failures > 0:
            raise DistutilsExecError('check failed.')


class run_install(base_install):
    def run(self):
        # The code must pass the tests before being installed
        self.run_command('check')
        base_install.run(self)


# Actual compilation

setup(name="python-recode",
      version=version,

      description="A Python extension to recode files",
      author="Frederic Gobry",
      author_email='gobry@pybliographer.org',
      url='http://pybliographer.org/',
      license='GPL',
      cmdclass={'check':   run_check,
                'install': run_install},
      long_description='''
This module contains a simple binding to GNU Recode.

It requires the GNU Recode 3.5 and its development header.

''',
      ext_modules=[
          Extension("recode", ["recodemodule.c"],
                    libraries=['recode'])
      ])
