import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/")
try:
	from metaclass import *
except:
	from metaclass25 import *

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

def plotap(inputfile):
	tfs_file = twiss(inputfile)
	x=tfs_file.X
	a=tfs_file.APER_1 
	z=tfs_file.Z
	l=tfs_file.L
	plot(z-l,x+a, color='black')
