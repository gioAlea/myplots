import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/")
sys.path.append("../../elements/")
sys.path.append("../../aperture/")
try:
	from metaclass import *
except:
	from metaclass25 import *
import elem
import aperture


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
#TWISS + SURVEY
#***************

tfs_file = twiss('madx/survey_lhcb1.tfs')
t1=tfs_file.THETA
z1=tfs_file.Z 
x1=tfs_file.X 

tfs_file = twiss('madx/coll_b1_ip8.tfs')

xa=tfs_file.X 
x=xa+x1


siga=(tfs_file.SIGXD + x)*1000
msiga=(-tfs_file.SIGXD + x)*1000
fsiga=(5*tfs_file.SIGXD + x)*1000
mfsiga=(-5*tfs_file.SIGXD + x)*1000

plot(z1,x*1000, color='blue', label='Beam 1')
plot(z1,siga, color='blue')
plot(z1,msiga, color='blue')
plot(z1,fsiga, color='blue')
plot(z1,mfsiga, color='blue')

fill_between(z1, siga, msiga, facecolor='blue')
fill_between(z1, siga, fsiga, facecolor='blue', alpha=0.2)
fill_between(z1, msiga, mfsiga, facecolor='blue', alpha=0.2)


tfs_file = twiss('madx/survey_lhcb2.tfs')
t2=tfs_file.THETA
z2=tfs_file.Z 
x2=tfs_file.X 

tfs_file = twiss('madx/coll_b2_ip8.tfs')

xb=tfs_file.X 
xx=xb+x2


sigb=(tfs_file.SIGXD + xx)*1000
msigb=(-tfs_file.SIGXD + xx)*1000
fsigb=(5*tfs_file.SIGXD + xx)*1000
mfsigb=(-5*tfs_file.SIGXD + xx)*1000

plot(z2, xx*1000, color='red', label='Beam 2')
plot(z2,sigb, color='red')
plot(z2,msigb, color='red')
plot(z2,fsigb, color='red')
plot(z2,mfsigb, color='red')

fill_between(z2, sigb, msigb, facecolor='red')
fill_between(z2, sigb, fsigb, facecolor='red', alpha=0.2)
fill_between(z2, msigb, mfsigb, facecolor='red', alpha=0.2)



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

#Element names to write in plot
e=('','D1','D2','D3','D4','Q2','Spectrometer','Compensator')

#Look at the readme_plotelem.txt
elem.plotelem(r'../../elements/out/aperture_b1_mbx.csv',D,t[3],e[1]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbxw.csv',D,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbrc.csv',D,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbrs.csv',D,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbw.csv',D,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mbrb.csv',D,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mqxa.csv',Q1,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mqxb.csv',Q2,t[3],e[5]) 
elem.plotelem(r'../../elements/out/aperture_b1_mc.csv',M,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_mk.csv',M,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_tc.csv',TC,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_b.csv',B,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_tan.csv',TAN,t[3],e[0]) 
elem.plotelem(r'../../elements/out/aperture_b1_tas.csv',TAN,t[3],e[0]) 
elem.plotv(r'../../elements/out/aperture_b1_v.csv',V,t[3],e[0]) 

# *********
# APERTURES
# *********

#aperture.plotap(r'madx/aperture_b1.tfs')


#********************	
#Plot characteristics
#********************

xlabel(r'z(m)')
ylabel(r'x(mm), $\sigma_x$, 5 $\sigma_x$')
xlim([-130,130])
ylim([-300,220])
grid(b=True, which='major',linestyle='--')
# l1 = legend(loc='lower right')
# l2 = legend([b6[0],b5[0],b1[0],b2[0],b3[0],b4[0]],['Dipoles','Quadrupoles','Vacuum Elements', 'LHCb Pipes', 'Collimators and Dump', 'Beam Instrumentation' ], loc='lower left')
# gca().add_artist(l1) # add l1 as a separate artist to the axes
# title(r'IP8 at collision')

show()
