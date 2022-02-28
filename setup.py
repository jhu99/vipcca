import setuptools
from setuptools import setup
from setuptools import Extension, dist, find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = [
      'scanpy',
      'tensorflow==2.4.0',
      'anndata',
      'scipy',
      'pandas',
      'seaborn',
      'keras',
      'python-igraph',
      'louvain',
      'h5py',
      'future'
]
setup(name='vipcca',
      version='0.2.7',
      description='single cell integration',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jhu99/vipcca',
      author='Jialu Hu',
      author_email='jialuhu@umich.edu',
      license='MIT',
      packages=find_packages(),
      install_requires=install_requires,
      zip_safe=False,
      python_requires='>=3.6',)
