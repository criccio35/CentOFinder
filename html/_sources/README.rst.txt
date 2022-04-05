* Written by Camila Riccio, Mauricio Peñuela, Camilo Rocha and Jorge Finke
* Last update: 04/04/22 

CentOFinder
-----------

This is a Python3 implementation to predict the centromere of rice chromosomes using CentO sequences.
The CentOFinder module takes as input a fasta file with a rice chromosome sequence, 
divide the chromosome into windows of the length indicated by the user (Kbp windows are usually used),
aligns the CentO sequence in the chromosome using the BLAST algorithm,
and detects de window with highest frecuency of CentO alignments.
As in rice the centromere is usually a region between 2 and 3 Mbp, the module predicts a centromeric
region for each of these longitudes based on the midpoint of the window with the highest frequency 
of CentO alignments.

Setup
------
Clone the repository::

  git clone git@github.com:criccio35/CentOFinder.git


Requirements
------------
Install the requirements by entering the following commands in the terminal:

Install biopython module::

  pip install biopython

Install Basic Local Alignment Search Tool (BLAST)::

  sudo apt update
  sudo apt install ncbi-blast+


Example
-------

The file **test.py**
contains an example that illustrates how to use the code to detect the 
centromere location in chromosome 01 of the *Oryza sativa* Indica Group cultivar:IR64.
Other IR64 chromosome sequences are available in the 
`NCBI Genome database <https://www.ncbi.nlm.nih.gov/genome>`_
under the accession number RWKJ00000000.

Below is a more detailed explanation of the same example:

Import module::

  import CentOFinder as cf

Input CentO fasta file path::

  CentO_path = 'input_data/CentO_AA.fasta'

Input chromosome fasta file path::

  chromosome_path = 'input_data/Osat_IR64_AGI_NSD_chrOK.id_chr01.fasta'

Input window size::

  size_w = 100_000

Instantiate the CentOFinder class::

  centromere = cf.CentOFinder(CentO_path, chromosome_path, size_w)

Call the method to detect the centromere::

  centromere.detect_centromere()

The above prints the following::

  Chromosome length: 44350042 base pairs
  Window size: 100000
  Total chromosome whindows: 443
  ----------------------------------------
  Approximate location of centromere:
  Window number: 178
  Window midpoint (base pair): 17850000
  2Mbp centromeric region prediction: [15850000,19850000]
  3Mbp centromeric region prediction: [14850000,20850000]

Plot the results

.. image:: Osat_IR64_chr01.png
  :width: 800
