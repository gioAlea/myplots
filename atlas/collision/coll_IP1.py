import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("../../elements/")
sys.path.append("../../")
import elem
import beams

params = {'backend': 'pdf',
	  	'font.size':20,	
          'axes.labelsize': 20,
          'legend.fontsize': 16,
          'xtick.labelsize': 20,
          'ytick.labelsize': 20,
	  'text.usetex':True,
         } 
          
rc('text.latex', preamble=r'\usepackage{cmbright}')
matplotlib.rcParams.update(params)


#***************
#PLOTTING BEAMS
#***************

beams.beam1x(r'madx/survey_lhcb1.tfs',r'madx/coll_b1_ip1.tfs')
beams.beam2x(r'madx/survey_lhcb2.tfs',r'madx/coll_b2_ip1.tfs')
# beams.beam1y(r'madx/survey_lhcb1.tfs',r'madx/coll_b1_ip5.tfs')
# beams.beam2y(r'madx/survey_lhcb2.tfs',r'madx/coll_b2_ip5.tfs')


#***************** 
#PLOTTING ELEMENTS
#*****************

#Color options
D='#419AD9'         #Dipoles: MBX, MBXW, MBRC, MBRS, MBW, MBRB
Q1='#249A27'        #MQXA
Q2='#55E058'        #MQXB
M='#EEBE4C'         #Kickers & Correctors: MC, MK
B='#9342AE'         #Beam Instrumentation: B
V='#A1AAA2'         #Vacuum elements
TC='#EE634C'        #Collimators
TAN='#8C3C2F'       #TAN & TAS
# spec='#9342AE'    #Spectrometers & compensators: MBAW, MBLW, MBWMD, MBXWH

#IP s(m) values
t=(0,3332.436584,13329.28923,23315.37898,0,3332.284216,13329.59397,23315.22662)

# t[0]    0               IP1 (ATLAS) for B1
# t[1]    3332.436584     IP2 (ALICE) for B1
# t[2]    13329.28923     IP5 (CMS) for B1
# t[3]    23315.37898     IP8 (LHCb) for B1
# t[4]    0               IP1 (ATLAS) for B2
# t[5]    3332.284216     IP2 (ALICE) for B2
# t[6]    13329.59397     IP5 (CMS) for B2
# t[7]    23315.22662     IP8 (LHCb) for B2

#Element names to write in plot
e=('','D1','D2','D3','D4','Q2','Spectrometer','Compensator')

#Look at the readme_plotelem.txt
elem.plotelem(r'../../elements/out/aperture_b1_mbx.csv',D,t[0],e[1]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbxw.csv',D,t[0],e[1]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbrc.csv',D,t[0],e[2]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbrs.csv',D,t[0],e[3]) 
# elem.plotelem(r'../../elements/out/aperture_b1_mbw.csv',D,t[0],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbrb.csv',D,t[0],e[4]) 
elem.plotelem(r'../../elements/out/aperture_b1_mqxa.csv',Q1,t[0],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mqxb.csv',Q2,t[0],e[5]) 
# elem.plotelem(r'../../elements/out/aperture_b1_mc.csv',M,t[0],e[0]) 
# elem.plotelem(r'../../elements/out/aperture_b1_mk.csv',M,t[0],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_tc.csv',TC,t[0],e[0]) 
# elem.plotelem(r'../../elements/out/aperture_b1_b.csv',B,t[0],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_tan.csv',TAN,t[0],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_tas.csv',TAN,t[0],e[0]) 
# elem.plotv(r'../../elements/out/aperture_b1_v.csv',V,t[0],e[0]) 

# *********
# APERTURES
# *********

#aperture.plotap(r'madx/aperture_b1.tfs')


#********************	
#Plot characteristics
#********************

xlabel(r'z(m)')
xlim([-130,130])
ylim([-100,150])
grid(b=True, which='major',linestyle='--')
# l1 = legend(loc='lower right')
# l2 = legend([b6[0],b5[0],b1[0],b2[0],b3[0],b4[0]],['Dipoles','Quadrupoles','Vacuum Elements', 'LHCb Pipes', 'Collimators and Dump', 'Beam Instrumentation' ], loc='lower left')
# gca().add_artist(l1) # add l1 as a separate artist to the axes
title(r'IP1 at collision (HL)')

show()

