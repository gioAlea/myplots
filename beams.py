import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/")
try:
	from metaclass import *
except:
	from metaclass25 import *

def beam1x(survey,twisss):
	tfs_file = twiss(survey)
	z=tfs_file.Z 
	x=(tfs_file.X)*1000 

	tfs_file = twiss(twisss)
	sigma=(tfs_file.SIGXD)*1000
	xt=(tfs_file.X)*1000 

	xtot=x+xt
	
	p=xtot+sigma 		#plus
	m=xtot-sigma		#minus
	fp=xtot+5*sigma 	#five plus
	fm=xtot-5*sigma		#five minus

	plot(z,xtot, color='blue', label='Beam 1')
	plot(z,p, color='blue')
	plot(z,m, color='blue')
	plot(z,fp, color='blue')
	plot(z,fm, color='blue')

	fill_between(z, p, m, facecolor='blue')
	fill_between(z, p, fp, facecolor='blue', alpha=0.2)
	fill_between(z, m, fm, facecolor='blue', alpha=0.2)

	xlabel(r'z(m)')
	ylabel(r'x(mm), $\sigma_x$, 5 $\sigma_x$')

def beam2x(survey,twisss):
	tfs_file = twiss(survey)
	z=tfs_file.Z 
	x=(tfs_file.X)*1000 

	tfs_file = twiss(twisss)
	sigma=(tfs_file.SIGXD)*1000
	xt=(tfs_file.X)*1000 

	xtot=x+xt

	p=xtot+sigma 		#plus
	m=xtot-sigma		#minus
	fp=xtot+5*sigma 	#five plus
	fm=xtot-5*sigma		#five minus

	plot(z,xtot, color='red', label='Beam 1')
	plot(z,p, color='red')
	plot(z,m, color='red')
	plot(z,fp, color='red')
	plot(z,fm, color='red')

	fill_between(z, p, m, facecolor='red')
	fill_between(z, p, fp, facecolor='red', alpha=0.2)
	fill_between(z, m, fm, facecolor='red', alpha=0.2)

	xlabel(r'z(m)')
	ylabel(r'x(mm), $\sigma_x$, 5 $\sigma_x$')

def beam1y(survey,twisss):
	tfs_file = twiss(survey)
	z=tfs_file.Z 
	y=(tfs_file.Y)*1000 

	tfs_file = twiss(twisss)
	sigma=(tfs_file.SIGYD)*1000
	yt=(tfs_file.Y)*1000 

	ytot=y+yt

	p=ytot+sigma 		#plus
	m=ytot-sigma		#minus
	fp=ytot+5*sigma 	#five plus
	fm=ytot-5*sigma	#five minus

	plot(z,ytot, color='blue', label='Beam 1')
	plot(z,p, color='blue')
	plot(z,m, color='blue')
	plot(z,fp, color='blue')
	plot(z,fm, color='blue')

	fill_between(z, p, m, facecolor='blue')
	fill_between(z, p, fp, facecolor='blue', alpha=0.2)
	fill_between(z, m, fm, facecolor='blue', alpha=0.2)

	xlabel(r'z(m)')
	ylabel(r'y(mm), $\sigma_y$, 5 $\sigma_y$')


def beam2y(survey,twisss):
	tfs_file = twiss(survey)
	z=tfs_file.Z 
	y=(tfs_file.Y)*1000 

	tfs_file = twiss(twisss)
	sigma=(tfs_file.SIGYD)*1000
	yt=(tfs_file.Y)*1000 

	ytot=y+yt

	p=ytot+sigma 		#plus
	m=ytot-sigma		#minus
	fp=ytot+5*sigma 	#five plus
	fm=ytot-5*sigma	#five minus

	plot(z,ytot, color='red', label='Beam 1')
	plot(z,p, color='red')
	plot(z,m, color='red')
	plot(z,fp, color='red')
	plot(z,fm, color='red')

	fill_between(z, p, m, facecolor='red')
	fill_between(z, p, fp, facecolor='red', alpha=0.2)
	fill_between(z, m, fm, facecolor='red', alpha=0.2)

	xlabel(r'z(m)')
	ylabel(r'y(mm), $\sigma_y$, 5 $\sigma_y$')
