.. vipcca documentation master file, created by
   sphinx-quickstart on Wed Dec 23 10:19:34 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

VIPCCA
=========================================================
Data alignment is one of the first key steps in single cell analysis for integrating multiple datasets and performing joint analysis across studies. Data alignment is challenging in extremely large datasets, however, as the major of the current single cell data alignment methods are not computationally efficient. Here, we present VIPCCA, a computational framework based on non-linear canonical correlation analysis for effective and scalable single cell data alignment. VIPCCA leverages both deep learning for effective single cell data modeling and variational inference for scalable computation, thus enabling powerful data alignment across multiple samples, multiple data platforms, and multiple data types. VIPCCA is accurate for a range of alignment tasks including alignment between single cell RNAseq and ATACseq datasets and can easily accommodate millions of cells, thereby providing researchers unique opportunities to tackle challenges emerging from large-scale single-cell atlas.


VIPCCA Installation
==================
.. toctree::
   :maxdepth: 2

   installation

VIPCCA Tutorial
==================
.. toctree::
   :maxdepth: 2
   
   tutorials/index.rst

VIPCCA API
==================  
.. toctree::
   :maxdepth: 2

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
