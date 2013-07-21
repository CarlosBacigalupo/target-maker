from constants import *
import numpy as np

global targetList

def reduce_targetList_by_PMax(targetList, PMax):
    
    
    targetList = targetList[targetList[PMaxCol] == PMax]
    

def add_lumin_to_targetList(targetList):

    parallax = targetList[parallaxCol]
    vMag = targetList[vMagCol]

    d = 1/parallax*1000 #mas/1000
    dMod = 5 * np.log10(d/10)
    aMag = vMag- dMod
        
    targetList[luminCol] =  np.exp((SOLAR_AMAG - aMag)/2.5)

    return targetList

def add_mass_to_targetList(targetList):

    lumin = targetList[luminCol]   
    mass = lumin**(1/4.5)
        
    targetList[massCol] =  mass

    return targetList

def add_PMax_to_tagetList(targetList):
    
    mass = targetList[massCol]
    temp = targetList[tempCol]
    lumin = targetList[luminCol]
    
    nuMax = ((mass * ((temp) ** 3.5)) / lumin) * (NU_MAX_SUN)
    
    PMax = 1/nuMax
    
    targetList[PMaxCol] = PMax
    
    return targetList

def add_temp_to_targetList(targetList):
    
#    V = targetList[VCol]
#    B = targetList[BCol]    
    CI = targetList[CICol]
    
    targetList[tempCol] = 8540/(CI + 0.865)/TEMP_EFF_SUN

    return targetList


def load_initial_data(catalogueFileName):
    
    a = np.loadtxt(catalogueFileName, unpack=True )

    return a


def add_columns(targetList, cols = 1):

     a = np.vstack((targetList, np.zeros((cols, len(targetList[0])))))
     
     return  a


def create_targetList():
    
    targetList = load_initial_data('initial_catalogue.txt')
    
    targetList = add_columns(targetList, cols = 4)
    
    targetList = add_temp_to_targetList(targetList)
    
    targetList = add_lumin_to_targetList(targetList)
    
    targetList = add_mass_to_targetList(targetList)
    
    targetList = add_PMax_to_tagetList(targetList)
    
    #print targetList
    #print 'end'

    return targetList
