import matplotlib
from matplotlib.pyplot import *
from matplotlib import rc
import sys
sys.path.append("/afs/cern.ch/eng/sl/lintrack/Python_Classes4MAD/")
try:
	from metaclass import *
except:
	from metaclass25 import *


#For Riccardos classes
#from draw2d import *
#from pyoptics import *



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


MQXA='#5F9EA0'
MQXB='#40E0D0'
MBX='#4E9A06'
MQM='#01A9DB'
LHCB='#8258FA'



#***************
#Twiss + Survey
#***************

tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/collision/survey_lhcb1.tfs')
t1=tfs_file.THETA
z1=tfs_file.Z 
x1=tfs_file.X 

tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/collision/coll_nm_b1.tfs')

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






tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/collision/survey_lhcb2.tfs')
t2=tfs_file.THETA
z2=tfs_file.Z 
x2=tfs_file.X 

tfs_file = twiss('/afs/cern.ch/user/a/ansantam/public/helmut/collision/coll_nm_b2.tfs')

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


#********** 
#ELEMENTS
#**********

data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_mqxa.csv',delimiter=',',dtype=str)

n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  b5=bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color=MQXA,edgecolor='black', linewidth='1.7',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
  
  
data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_mqxb.csv',delimiter=',',dtype=str)

n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color=MQXA,edgecolor='black',linewidth='1.7',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
  
  
  
data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_mqm_mqy.csv',delimiter=',',dtype=str)

n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color=MQXA,edgecolor='black',linewidth='1.7',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
  
data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_mbx.csv',delimiter=',',dtype=str)

n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  b6=bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color=MBX,edgecolor='black',linewidth='1.7',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_tan_tas.csv',delimiter=',',dtype=str)  

n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  # bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color='black',edgecolor='black',linewidth='1.3',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_vacuum.csv',delimiter=',',dtype=str)  
n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  b1=bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color='grey',edgecolor='grey',linewidth='1.3',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)

data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_pipe.csv',delimiter=',',dtype=str)  
n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  b2=bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color='purple',edgecolor='purple',linewidth='1.3',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)

data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_t.csv',delimiter=',',dtype=str)  
n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  b3=bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color='blue',edgecolor='blue',linewidth='1.3',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)

data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/geometry/elements/backup/el_beamins.csv',delimiter=',',dtype=str)  
n,s0,l0=[],[],[]
for d in data:
  a=str(d[0])
  s0=float(d[1])
  l0=float(d[2])
  b4=bar(s0- 23315.37898-l0,300, width=l0,bottom=-150,color='orange',edgecolor='orange',linewidth='1.3',alpha=0.3)
  # annotate(a.strip('"'),xy=(s0- 23315.37898-l0,150), xytext=(s0- 23315.37898-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
  # 
  
# data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/names.csv',delimiter=',',dtype=str)  
# n,s0=[],[]
# for d in data:
#   a=str(d[0])
#   s0=float(d[1])
#   annotate(a.replace('.B1', ''),xy=(s0-l0,150), xytext=(s0-(l0/2),151),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
#   




# annotate(r'Spectrometer',xy=(5.5,105), xytext=(5.5,105),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
annotate(r'Q1',xy=(26,130), xytext=(26,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q2',xy=(38,130), xytext=(38,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q3',xy=(50,130), xytext=(50,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'D1',xy=(63,130), xytext=(63,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'D2',xy=(127,130), xytext=(127,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q4',xy=(139.5,130), xytext=(139.5,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q5',xy=(169.5,130), xytext=(169.5,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q1',xy=(-26,130), xytext=(-26,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q2',xy=(-38,130), xytext=(-38,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q3',xy=(-50,130), xytext=(-50,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'D1',xy=(-63,130), xytext=(-63,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'D2',xy=(-127,130), xytext=(-127,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q4',xy=(-139.5,130), xytext=(-139.5,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
annotate(r'Q5',xy=(-169.5,130), xytext=(-169.5,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')

#TAN
# bar(120,130, width=0.77,bottom=-65,color='black',edgecolor='black',linewidth='1.3',alpha=0.6)
# bar(110,40, width=0.77,bottom=85,color='black',edgecolor='black',linewidth='1.3',alpha=0.6)
# annotate(r'TAN',xy=(110,130), xytext=(110,130),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=15)
# bar(110,-40, width=0.77,bottom=-85,color='black',edgecolor='black',linewidth='1.3',alpha=0.6)






#********************************************** 
#APERTURES WITH VACUUM CHAMBERS AND BEAM PIPES
#**********************************************

data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b1_up.csv',delimiter=',',dtype=str)

z1u,x1u=[],[]
for d in data:
  z1u.append(d[0])
  x1u.append(d[1])


plot(z1u,x1u,color='black', linewidth='2.0',label=r'Apertures with VC and beampipes')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b1_down.csv',delimiter=',',dtype=str)

z1d,x1d=[],[]
for d in data:
  z1d.append(d[0])
  x1d.append(d[1])

plot(z1d,x1d,color='black', linewidth='2.0')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b2_up.csv',delimiter=',',dtype=str)

z2u,x2u=[],[]
for d in data:
  z2u.append(d[0])
  x2u.append(d[1])


plot(z2u,x2u,color='black', linewidth='2.0')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b2_down.csv',delimiter=',',dtype=str)

z2d,x2d=[],[]
for d in data:
  z2d.append(d[0])
  x2d.append(d[1])

plot(z2d,x2d,color='black', linewidth='2.0')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b1_up_left.csv',delimiter=',',dtype=str)

z1u,x1u=[],[]
for d in data:
  z1u.append(d[0])
  x1u.append(d[1])


plot(z1u,x1u,color='black', linewidth='2.0')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b1_down_left.csv',delimiter=',',dtype=str)

z1d,x1d=[],[]
for d in data:
  z1d.append(d[0])
  x1d.append(d[1])

plot(z1d,x1d,color='black', linewidth='2.0')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b2_up_left.csv',delimiter=',',dtype=str)

z2u,x2u=[],[]
for d in data:
  z2u.append(d[0])
  x2u.append(d[1])


plot(z2u,x2u,color='black', linewidth='2.0')


data=np.loadtxt(r'/afs/cern.ch/user/a/ansantam/public/helmut/collision/apertures_b2_down_left.csv',delimiter=',',dtype=str)

z2d,x2d=[],[]
for d in data:
  z2d.append(d[0])
  x2d.append(d[1])

plot(z2d,x2d,color='black', linewidth='2.0')







#********** 
#NEUTRALS
#**********

x=numpy.linspace(-300,0,100)
y=numpy.tan(0.000115)*x*1000
plot(x,y,color='orange', linewidth='1.0', label=r'Neutrals')

x1=numpy.linspace(-300,0,100)
y1=numpy.tan(0.000165)*x*1000
plot(x1,y1,color='orange')

x2=numpy.linspace(-300,0,100)
y2=numpy.tan(0.000065)*x*1000
plot(x2,y2,color='orange')


fill_between(x,y1, y2, facecolor='orange', alpha=0.4)


x=-numpy.linspace(-300,0,100)
y=-numpy.tan(0.000115)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=-numpy.linspace(-300,0,100)
y1=-numpy.tan(0.000165)*x*1000
plot(x1,y1,color='orange')

x2=-numpy.linspace(-300,0,100)
y2=-numpy.tan(0.000065)*x*1000
plot(x2,y2,color='orange')

fill_between(x,y1, y2, facecolor='orange', alpha=0.4)

x=numpy.linspace(-300,0,100)
y=numpy.tan(0.0003849)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=numpy.linspace(-300,0,100)
y1=numpy.tan(0.0003349)*x*1000
plot(x1,y1,color='orange')

x2=numpy.linspace(-300,0,100)
y2=numpy.tan(0.0004349)*x*1000
plot(x2,y2,color='orange')

fill_between(x,y1, y2, facecolor='orange', alpha=0.4)

x=-numpy.linspace(-300,0,100)
y=-numpy.tan(0.0003849)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=-numpy.linspace(-300,0,100)
y1=-numpy.tan(0.0003349)*x*1000
plot(x1,y1,color='orange')

x2=-numpy.linspace(-300,0,100)
y2=-numpy.tan(0.0004349)*x*1000
plot(x2,y2,color='orange')

fill_between(x,y1, y2, facecolor='orange', alpha=0.4)

x=numpy.linspace(-300,0,100)
y=numpy.tan(0.000115)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=numpy.linspace(-300,0,100)
y1=numpy.tan(0.000165)*x*1000
plot(x1,y1,color='orange')

x2=numpy.linspace(-300,0,100)
y2=numpy.tan(0.000065)*x*1000
plot(x2,y2,color='orange')


fill_between(x,y1, y2, facecolor='orange', alpha=0.4)


x=-numpy.linspace(-300,0,100)
y=-numpy.tan(0.000115)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=-numpy.linspace(-300,0,100)
y1=-numpy.tan(0.000165)*x*1000
plot(x1,y1,color='orange')

x2=-numpy.linspace(-300,0,100)
y2=-numpy.tan(0.000065)*x*1000
plot(x2,y2,color='orange')

fill_between(x,y1, y2, facecolor='orange', alpha=0.4)

x=numpy.linspace(-300,0,100)
y=numpy.tan(0.0003849)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=numpy.linspace(-300,0,100)
y1=numpy.tan(0.0003349)*x*1000
plot(x1,y1,color='orange')

x2=numpy.linspace(-300,0,100)
y2=numpy.tan(0.0004349)*x*1000
plot(x2,y2,color='orange')

fill_between(x,y1, y2, facecolor='orange', alpha=0.4)

x=-numpy.linspace(-300,0,100)
y=-numpy.tan(0.0003849)*x*1000
plot(x,y,color='orange', linewidth='1.0')

x1=-numpy.linspace(-300,0,100)
y1=-numpy.tan(0.0003349)*x*1000
plot(x1,y1,color='orange')

x2=-numpy.linspace(-300,0,100)
y2=-numpy.tan(0.0004349)*x*1000
plot(x2,y2,color='orange')

fill_between(x,y1, y2, facecolor='orange', alpha=0.4)




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








