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
                           'BACK_REACTION',
                           'TWO_FACES', 
                           'FLUX_CORRECTION',
                           'NBS_CLOUD',
                           'RETIRE_FLAG',
                           'CUST_SCHEDULE']
                floatList = ["V_MU", 
                             "V_SIGMA", 
                             "M_MU", 
                             "M_SIGMA", 
                             'WIND_MU',
                             'R_MIN',
                             'R_START', 
                             'R_DELTA', 
                             'SONIC_POINT', 
                             'SFR', 
                             'EDOT', 
                             'ALPHA', 
                             'BETA', 
                             'CLOUD_MASS', 
                             'WIND_METALLICITY', 
                             'CLOUD_METALLICITY',
                             'CLOUD_TEMP', 
                             'F_TURB0', 
                             'MDOT_CHI_POWER', 
                             'E_SN',
                             'M_PER_SN', 
                             'CLOUD_ALPHA', 
                             'V_CIR', 
                             'RETIREMENT_MASS',
                             'CFL_MC',
                             'POWER_LAW_MAX_MASS',
                             'POWER_LAW_MIN_MASS',
                             'POWER_LAW_SLOPE', 
                             'TURBULENT_VELOCITY_CHI_POWER', 
                             'GEOMETRIC_FACTOR', 
                             'COOLING_AREA_CHI_POWER', 
                             'COLD_TURBULENCE_CHI_POWER',
                             'MDOT_COEFFICIENT',
                             'DRAG_COEFF', 
                             'M_CLOUD_MIN']
                if pline[0] in intList:
                    self.paramDict[pline[0]]=int(pline[1])
                elif pline[0] in floatList:
                    self.paramDict[pline[0]]=float(pline[1])
                else:
                    self.paramDict[pline[0]]=pline[1]
        fp.close

        self.paramDict['RETIREMENT_MASS'] *= const.Msun
        self.paramDict['M_CLOUD_MIN'] *= const.Msun        
        self.paramDict['WIND_METALLICITY'] *= const.ZSun
        self.paramDict['CLOUD_METALLICITY'] *= const.ZSun        
        self.paramDict['V_CIR'] = self.paramDict['V_CIR'] * const.km / const.s
        self.paramDict['GAMMA'] = 5/3        
        self.paramDict['R_MIN'] = self.paramDict['R_MIN'] * const.pc
        self.paramDict['R_START'] = self.paramDict['R_START'] * const.pc
        self.paramDict['R_DELTA'] = self.paramDict['R_DELTA'] * const.pc        
        self.paramDict['SONIC_POINT'] = self.paramDict['SONIC_POINT'] * const.pc
        self.paramDict['SFR'] = self.paramDict['SFR'] * const.Msun / const.yr
        self.paramDict['MDOT']= self.paramDict['BETA'] * self.paramDict['SFR']
        self.paramDict['M_PER_SN'] = self.paramDict['M_PER_SN'] * const.Msun
        self.paramDict['EDOT'] = self.paramDict['ALPHA'] * self.paramDict['E_SN'] * self.paramDict['SFR'] / self.paramDict['M_PER_SN'] 
        
        import pickle
        with open('cust_schedule.obj','rb') as file_object:
            raw_data = pickle.load(file_object)
        self.paramDict['CUSTOM_SCHEDULE'] = raw_data
        