######################################################################
# 
# Author    : Anthony Chow
# Date      : 11th May 2021
#
# File name : param.py
#
# Description : Class definition for object to hold paramters for 
#               multiphase wind structure
#
######################################################################

import math


class Param:

    # Parameter object initialization
    # Read parameters from input files
    # Create dictionary of parameters 
    def __init__(self, inputFile, const):
        self.paramDict = {}
        fp = open("inputs")
        for line in fp:
            pline = line.replace("=","").split()
            if pline != [] and len(pline) > 1:
                intList = ["V_CELLS", 
                           "M_CELLS",
                           "R_CELLS", 
                           "V_MAX", 
                           "V_MIN", 
                           "M_MAX", 
                           "M_MIN", 
                           'R_STEPS', 
                           'BACK_REACTION']
                floatList = ["V_MU", 
                             "V_SIGMA", 
                             "M_MU", 
                             "M_SIGMA", 
                             'WIND_MU', 
                             'R_START', 
                             'R_DELTA', 
                             'SONIC_POINT', 
                             'SFR', 
                             'EDOT', 
                             'ALPHA', 
                             'BETA', 
                             'CLOUD_MASS', 
                             'METALLICITY', 
                             'CLOUD_TEMP', 
                             'F_TURB0', 
                             'MDOT_CHI_POWER', 
                             'E_SN',
                             'M_PER_SN', 
                             'CLOUD_ALPHA']
                if pline[0] in intList:
                    self.paramDict[pline[0]]=int(pline[1])
                elif pline[0] in floatList:
                    self.paramDict[pline[0]]=float(pline[1])
                else:
                    self.paramDict[pline[0]]=pline[1]
        fp.close

        self.paramDict['GAMMA'] = 5/3
        self.paramDict['R_START'] = self.paramDict['R_START'] * const.pc
        self.paramDict['R_DELTA'] = self.paramDict['R_DELTA'] * const.pc        
        self.paramDict['SONIC_POINT'] = self.paramDict['SONIC_POINT'] * const.pc
        self.paramDict['SFR'] = self.paramDict['SFR'] * const.Msun / const.yr
        self.paramDict['MDOT']= self.paramDict['BETA'] * self.paramDict['SFR']
        self.paramDict['M_PER_SN'] = self.paramDict['M_PER_SN'] * const.Msun
        self.paramDict['EDOT'] = self.paramDict['ALPHA'] * self.paramDict['E_SN'] * self.paramDict['SFR'] / self.paramDict['M_PER_SN'] 
        
