import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("../../elements/")
sys.path.append("../../")
import elem
import param

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

param.beamx(r'madx/param_b1_ip5.tfs',r'madx/param_b2_ip5.tfs',t[2],t[6])

param.beamy(r'madx/param_b1_ip5.tfs',r'madx/param_b2_ip5.tfs',t[2],t[6])

param.beta(r'madx/param_b1_ip5.tfs',t[2])

param.angle(r'madx/param_b1_ip5.tfs',t[2])

show()


