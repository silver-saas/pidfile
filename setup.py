from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def readme():
    with open('README.md') as readme_file:
        return readme_file.read()


setup(
    name='pidfile',
    version='0.0.1',
    description='A module for interacting with pidfiles',
    long_description=readme(),
    keywords='system pidfile pid process',
    url='http://github.com/silver-saas/pidfile',
    author='Horia Coman',
    author_email='horia141@gmail.com',
    license='All right reserved',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    test_suite='tests',
    tests_require=[],
    include_package_data=True,
    zip_safe=False
)
