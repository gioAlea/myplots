from matplotlib.pyplot import *

def plotelem(inputfile,color,ip,elem):
  data=np.loadtxt(inputfile,delimiter=',',dtype=str)
  n,s0,l0=[],[],[]
  for d in data:
    a=str(d[0])
    s0=float(d[1])
    l0=float(d[2])
    b=s0-l0-ip
    bar(b,200, width=l0,bottom=-100,color=color,edgecolor='black', linewidth='1.7',alpha=0.3)
    annotate(a,xy=(b,100), xytext=(s0-(l0/2)-ip,101),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',rotation=90,size=10)
    annotate(elem,xy=(s0-(l0/2)-ip,70), xytext=(s0-(l0/2)-ip,70),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
    annotate(r'Q1',xy=(26,70), xytext=(26,70),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
    annotate(r'Q3',xy=(50,70), xytext=(50,70),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
    annotate(r'Q1',xy=(-26,70), xytext=(-26,70),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')
    annotate(r'Q3',xy=(-50,70), xytext=(-50,70),name='Verdana',family='sans-serif',weight='heavy', va='bottom', ha='center',size=15,fontweight='bold')

def plotv(inputfile,color,ip,elem):
  data=np.loadtxt(inputfile,delimiter=',',dtype=str)
  n,s0,l0=[],[],[]
  for d in data:
    s0=float(d[1])
    l0=float(d[2])
    b=s0-l0-ip
    bar(b,200, width=l0,bottom=-100,color=color,edgecolor='black', linewidth='1.7',alpha=0.3)