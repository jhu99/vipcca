# Variational Inference assisted non-linear Probabilistic CCA (VIPCCA)

 [![Documentation Status](https://readthedocs.org/projects/vipcca/badge/?version=latest)](https://vipcca.readthedocs.io/en/latest/?badge=latest) ![PyPI](https://img.shields.io/pypi/v/vipcca?color=blue) [![Downloads](https://pepy.tech/badge/vipcca)](https://pepy.tech/project/vipcca) ![GitHub Repo stars](https://img.shields.io/github/stars/jhu99/vipcca?color=yellow)


### Description

Data alignment is one of the first key steps in single cell analysis for integrating multiple datasets and performing joint analysis across studies. Data alignment is challenging in extremely large datasets, however, as the major of the current single cell data alignment methods are not computationally efficient. Here, we present VIPCCA, a computational framework based on non-linear canonical correlation analysis for effective and scalable single cell data alignment. VIPCCA leverages both deep learning for effective single cell data modeling and variational inference for scalable computation, thus enabling powerful data alignment across multiple samples, multiple data platforms, and multiple data types. VIPCCA is accurate for a range of alignment tasks including alignment between single cell RNAseq and ATACseq datasets and can easily accommodate millions of cells, thereby providing researchers unique opportunities to tackle challenges emerging from large-scale single-cell atlas. 

### Citation

Jialu Hu, Mengjie Chen, Xiang Zhou, Effective and scalable single-cell data alignment with non-linear canonical correlation analysis, Nucleic Acids Research, Volume 50, Issue 4, 28 February 2022, Page e21, https://doi.org/10.1093/nar/gkab1147

### Installation

- Create conda environment

  ```shell
  $ conda create -n vipcca python=3.8
  $ conda activate vipcca
  ```

- Install VIPCCA from pypi

  ```shell
  $ pip install vipcca
  ```

- Alternatively, install the develop version of VIPCCA from GitHub source code

  ```shell
  $ git clone https://github.com/jhu99/vipcca.git
  $ cd ./vipcca/
  $ python -m pip install .
  ```

**Note**: Please make sure your python version >= 3.7, and install tensorflow-gpu if GPU is available on your your machine.

### Usage of vipcca

For a quick start, please follow our guide about the usage of VIPCCA in the [**Tutorial and Documentation**](https://vipcca.readthedocs.io/en/latest/) pages.



