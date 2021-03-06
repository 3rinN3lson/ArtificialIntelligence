#!/usr/bin/python
# -*- coding: utf-8 -*-

someTestStates = [
['NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'C_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_0', 'NV_2_1', 'C_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_1', 'NV_3_2', 'NV_3_3'],
['NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['C_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['-C_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'C_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['NV_0_0', '-C_0_1', 'NV_0_2', 'NV_0_3', '-C_1_0', 'C_1_1', 'NV_1_2', 'NV_1_3', '-C_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', '-C_3_3'],
['NV_0_0', 'NV_0_1', 'C_0_2', 'NV_0_3', '-C_1_0', '-C_1_1', '-C_1_2', 'C_1_3', 'NV_2_0', 'NV_2_1', '-C_2_2', '-C_2_3', '-C_3_0', '-C_3_1', '-C_3_2', '-C_3_3'],
['-C_0_0', 'NV_0_1', '-C_0_2', '-C_0_3', 'C_1_0', '-C_1_1', '-C_1_2', '-C_1_3', 'NV_2_0', 'C_2_1', '-C_2_2', '-C_2_3', 'C_3_0', 'NV_3_1', '-C_3_2', '-C_3_3'],
['-C_0_0', 'NV_0_1', '-C_0_2', '-C_0_3', 'NV_1_0', 'NV_1_1', '-C_1_2', 'NV_1_3', 'C_2_0', 'NV_2_1', 'C_2_2', 'NV_2_3', '-C_3_0', 'NV_3_1', '-C_3_2', '-C_3_3'],
['-C_0_0', '-C_0_1', 'NV_0_2', '-C_0_3', 'NV_1_0', 'C_1_1', '-C_1_2', 'NV_1_3', 'C_2_0', 'NV_2_1', 'NV_2_2', '-C_2_3', '-C_3_0', 'C_3_1', '-C_3_2', '-C_3_3'],
['NV_0_0', 'C_0_1', 'NV_0_2', '-C_0_3', 'C_1_0', 'NV_1_1', '-C_1_2', 'NV_1_3', '-C_2_0', '-C_2_1', 'NV_2_2', 'NV_2_3', 'NV_3_0', '-C_3_1', 'NV_3_2', '-C_3_3'],
['-C_0_0', 'C_0_1', '-C_0_2', '-C_0_3', 'C_1_0', 'NV_1_1', 'NV_1_2', '-C_1_3', '-C_2_0', 'NV_2_1', 'NV_2_2', 'NV_2_3', 'NV_3_0', '-C_3_1', '-C_3_2', '-C_3_3'],
['NV_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'C_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_0', 'NV_2_1', 'C_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_1', 'NV_3_2', 'NV_3_3'],
['C_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'NV_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['-C_0_0', 'NV_0_1', 'NV_0_2', 'NV_0_3', 'NV_1_0', 'NV_1_1', 'NV_1_2', 'C_1_3', 'NV_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', 'NV_3_3'],
['NV_0_0', '-C_0_1', 'NV_0_2', 'NV_0_3', '-C_1_0', 'C_1_1', 'NV_1_2', 'NV_1_3', '-C_2_1', 'NV_2_0', 'NV_2_2', 'NV_2_3', 'NV_3_0', 'NV_3_2', 'NV_3_1', '-C_3_3'],
['-C_0_0', 'NV_0_1', 'NV_0_2', '-C_0_3', '-C_1_0', '-C_1_1', '-C_1_2', 'NV_1_3', 'NV_2_0', 'C_2_1', '-C_2_2', '-C_2_3', 'C_3_0', 'NV_3_1', 'C_3_2', '-C_3_3'],
['-C_0_0', 'NV_0_1', '-C_0_2', 'C_0_3', '-C_1_0', 'NV_1_1', 'C_1_2', 'NV_1_3', 'NV_2_0', '-C_2_1', '-C_2_2', 'C_2_3', '-C_3_0', '-C_3_1', 'NV_3_2', '-C_3_3'],
['C_0_0', 'NV_0_1', 'NV_0_2', '-C_0_3', '-C_1_0', 'C_1_1', '-C_1_2', 'NV_1_3', '-C_2_0', '-C_2_1', '-C_2_2', '-C_2_3', '-C_3_0', '-C_3_1', 'NV_3_2', '-C_3_3'],
['-C_0_0', '-C_0_1', 'C_0_2', 'NV_0_3', '-C_1_0', '-C_1_1', '-C_1_2', 'NV_1_3', 'NV_2_0', '-C_2_1', '-C_2_2', '-C_2_3', '-C_3_0', '-C_3_1', '-C_3_2', 'NV_3_3'],
['NV_0_0', '-C_0_1', '-C_0_2', 'NV_0_3', '-C_1_0', '-C_1_1', 'NV_1_2', 'NV_1_3', '-C_2_0', '-C_2_1', 'C_2_2', 'NV_2_3', '-C_3_0', 'C_3_1', 'NV_3_2', 'C_3_3'],
['-C_0_0', '-C_0_1', '-C_0_2', '-C_0_3', 'NV_1_0', '-C_1_1', '-C_1_2', 'NV_1_3', 'C_2_0', '-C_2_1', '-C_2_2', 'NV_2_3', 'NV_3_0', 'C_3_1', 'NV_3_2', 'NV_3_3']
]