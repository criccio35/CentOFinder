#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  18 13:04:20 2022

@author: camila Riccio and Mauricio Peñuela
"""

!pip install biopython
!sudo apt install ncbi-blast+

import CentOFinder as cf

CentO_path = 'input_data/CentO_AA.fasta'
chromosome_path = 'input_data/Osat_IR64_AGI_NSD_chrOK.id_chr01.fasta'
size_w = 200_000

centromere = cf.CentOFinder(CentO_path, chromosome_path, size_w)
centromere.detect_centromere()
centromere.plot_CentO_frequency()