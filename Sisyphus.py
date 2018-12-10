# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy
import pandas
from crpapi import CRP
from crpapi import CRPApiError

CRP.apikey = 'b7019f6be56c4ea1b14fa6a630209018'

print(CRP.getLegislators.get(id='NJ04'))


