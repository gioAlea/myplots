from matplotlib import rc
from matplotlib.pyplot import *
import sys
sys.path.append("/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/")
try:
	from metaclass import *
except:
	from metaclass25 import *



params = {'backend': 'pdf',
          'font.family':'Tahoma',
	  'font.size':20,	
          'axes.labelsize': 17,
          'legend.fontsize': 16,
          'xtick.labelsize': 16,
          'ytick.labelsize': 16,
	  'text.usetex':True,
         } 
          
rc('text.latex', preamble=r'\usepackage{cmbright}')
matplotlib.rcParams.update(params)

tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/injection/inj_nm_b1.tfs')

fig=figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(223)
ax3=fig.add_subplot(222)
ax4=fig.add_subplot(224)


s=tfs_file.S - 23315.37898
y1=(tfs_file.X + 5*tfs_file.SIGXD)*1000
y2=(tfs_file.X - 5*tfs_file.SIGXD)*1000
y11=(tfs_file.X + tfs_file.SIGXD)*1000
y21=(tfs_file.X - tfs_file.SIGXD)*1000

ax1.plot(s,y11,color='blue',label=r'Beam 1')
ax1.plot(s,y21,color='blue')
ax1.plot(s,y1,color='blue')
ax1.plot(s,y2,color='blue')
ax1.fill_between(s, y11, y21, facecolor='blue')
ax1.fill_between(s, y11, y1, facecolor='blue', alpha=0.3)
ax1.fill_between(s, y21, y2, facecolor='blue', alpha=0.3)


tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/injection/inj_nm_b2.tfs')

s=tfs_file.S - 23315.22662
y1=(tfs_file.X + 5*tfs_file.SIGXD)*1000
y2=(tfs_file.X - 5*tfs_file.SIGXD)*1000
y11=(tfs_file.X + tfs_file.SIGXD)*1000
y21=(tfs_file.X - tfs_file.SIGXD)*1000


ax1.plot(s,y11,color='red',label=r'Beam 2')
ax1.plot(s,y21,color='red')
ax1.plot(s,y1,color='red')
ax1.plot(s,y2,color='red')
ax1.fill_between(s, y11, y21,facecolor='red')
ax1.fill_between(s, y11, y1, facecolor='red', alpha=0.3)
ax1.fill_between(s, y21, y2, facecolor='red', alpha=0.3)

ax1.set_xlabel(r's(m)')
ax1.set_ylabel(r'X(mm), $\sigma_x$, 5 $\sigma_x$')
ax1.set_title(r'IP8 / Injection / Nominal Values/ SPEC=1')
ax1.set_xlim([-150,150])
ax1.set_ylim([-20,20])
ax1.grid(b=True, which='major',linestyle='--')
ax1.legend(loc='lower right')



tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/injection/inj_nm_b1.tfs')

s=tfs_file.S - 23315.37898
y1=(tfs_file.Y+ 5*tfs_file.SIGYD)*1000
y2=(tfs_file.Y - 5*tfs_file.SIGYD)*1000
y11=(tfs_file.Y + tfs_file.SIGYD)*1000
y21=(tfs_file.Y - tfs_file.SIGYD)*1000

ax2.plot(s,y11,color='blue', label=r'Beam 1')
ax2.plot(s,y21,color='blue')
ax2.plot(s,y1,color='blue')
ax2.plot(s,y2,color='blue')
ax2.fill_between(s, y11, y21,facecolor='blue')
ax2.fill_between(s, y11, y1, facecolor='blue', alpha=0.3)
ax2.fill_between(s, y21, y2, facecolor='blue', alpha=0.3)



tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/injection/inj_nm_b2.tfs')

s=tfs_file.S - 23315.22662
y1=(tfs_file.Y + 5*tfs_file.SIGYD)*1000
y2=(tfs_file.Y - 5*tfs_file.SIGYD)*1000
y11=(tfs_file.Y + tfs_file.SIGYD)*1000
y21=(tfs_file.Y - tfs_file.SIGYD)*1000


ax2.plot(s,y11,color='red',label=r'Beam 2')
ax2.plot(s,y21,color='red')
ax2.plot(s,y1,color='red')
ax2.plot(s,y2,color='red')
ax2.fill_between(s, y11, y21, facecolor='red')
ax2.fill_between(s, y11, y1, facecolor='red', alpha=0.3)
ax2.fill_between(s, y21, y2, facecolor='red', alpha=0.3)

ax2.set_xlabel(r's(m)')
ax2.set_ylabel(r'Y(mm), $\sigma_y$, 5 $\sigma_y$')
ax2.set_xlim([-150,150])
ax2.set_ylim([-20,20])
ax2.grid(b=True, which='major',linestyle='--')
ax2.legend(loc='lower right')
ax2.annotate('y=-3.5 mm', xy=(0,-3.5), xytext=(0,-100), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->',  
                            color='black'))



tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/injection/inj_nm_b1.tfs')

s=tfs_file.S - 23315.37898
bx=tfs_file.BETX
by=tfs_file.BETY

ax3.plot(s,bx,color='blue', label=r'$\beta_x$')
ax3.plot(s,by,color='green', label=r'$\beta_y$')
ax3.set_xlabel(r's(m)')
ax3.set_ylabel('Beta functions (m)')
ax3.set_xlim([-150,150])
ax3.set_ylim([-50,300])
ax3.grid(b=True, which='major',linestyle='--')
ax3.legend(loc='lower right')
ax3.annotate(r'$\beta^*=10$', xy=(0,10), xytext=(-50,-40), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->',  
                            color='black'))


tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/injection/inj_nm_b1.tfs')

s=tfs_file.S - 23315.37898
px=tfs_file.PX*1000000
py=tfs_file.PY*1000000
ax4.plot(s,px,color='red', label=r'Effective angle in x')
ax4.plot(s,py,color='purple', label=r'Effective angle in y')
ax4.set_xlabel(r's(m)')
ax4.set_ylabel('Effective angle ($\mu$ rad)')
ax4.set_xlim([-150,150])
ax4.grid(b=True, which='major',linestyle='--')
ax4.legend(loc='lower right')
ax4.annotate('py=-2 $\mu$rad', xy=(0,-2), xytext=(-120,70), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->',  
                            color='black'))
ax4.annotate('px=1930 $\mu$rad', xy=(0,1930), xytext=(-120,-30), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->',  
                            color='black'))    

show()
