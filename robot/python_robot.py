import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Create the time array
t0=0
t_end=1
dt=0.005
t=np.arange(t0,t_end+dt,dt)

# Joint 1
r1=4+0*t
f1=1
alpha1=2*np.pi*f1*t
x1=(r1)*np.cos(alpha1)
y1=(r1)*np.sin(alpha1)

# Joint 2
r2=3
f2=1
alpha2=2*np.pi*f2*t # With respect to the 1st joint
dx1=(r2)*np.cos(alpha2+alpha1)
dy1=(r2)*np.sin(alpha2+alpha1)
x2=x1+dx1
y2=y1+dy1

# Joint 3
r3=2
f3=1
alpha3=2*np.pi*f3*t
dx2=(r3)*np.cos(alpha3+alpha2+alpha1)
dy2=(r3)*np.sin(alpha3+alpha2+alpha1)
x3=x2+dx2
y3=y2+dy2

################################## ANIMATION #################################

frame_amount=len(t)
def update_plot(num):
    joint_1.set_data([0,x1[num]],[0,y1[num]])
    joint_2.set_data([x1[num],x2[num]],[y1[num],y2[num]])
    joint_3.set_data([x2[num],x3[num]],[y2[num],y3[num]])
    trajectory.set_data(x3[0:num],y3[0:num])

    length_j1_funct.set_data(t[0:num],r1[0:num])
    alpha1_funct.set_data(t[0:num],alpha1[0:num])
    alpha2_funct.set_data(t[0:num],alpha2[0:num])
    return joint_1,joint_2,joint_3,trajectory,length_j1_funct,alpha1_funct,alpha2_funct

# Define figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(3,3)
plt.subplots_adjust(left=0.03,bottom=0.035,right=0.99,top=0.97,wspace=0.15,hspace=0.2)

# Subplot 1
ax1=fig.add_subplot(gs[:,0:2],facecolor=(0.9,0.9,0.9))
base_line,=ax1.plot([0,0],[0,0.4],'k',linewidth=20,alpha=0.5)
joint_1,=ax1.plot([],[],'k',linewidth=4)
joint_2,=ax1.plot([],[],'b',linewidth=4)
joint_3,=ax1.plot([],[],'g',linewidth=4)
trajectory,=ax1.plot([],[],'r',linewidth=2)
ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position(('center'))
ax1.xaxis.set_label_coords(0.5, -0.01)
ax1.yaxis.set_label_coords(-0.002, 0.5)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xticks(np.arange(-10,10+1,1))
plt.yticks(np.arange(-10,10+1,1))
plt.xlabel('meters [m]',fontsize=12)
plt.ylabel('meters [m]',fontsize=12)
plt.grid(True)

copyright=ax1.text(-10,10*1.01,'© Nhat Vu',size=10)

# Subplot 2
ax2=fig.add_subplot(gs[0,2],facecolor=(0.9,0.9,0.9))
length_j1_funct,=ax2.plot([],[],'b',linewidth=2)
plt.xlim(t0,t_end)
plt.ylim(0,r1[-1]+1)
plt.xlabel('time [s]',fontsize=12)
plt.ylabel('meters [m]',fontsize=12)
plt.grid(True)

# Subplot 3
ax3=fig.add_subplot(gs[1,2],facecolor=(0.9,0.9,0.9))
alpha1_funct,=ax3.plot([],[],'b',linewidth=2)
plt.xlim(t0,t_end)
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])
plt.xlabel('time [s]',fontsize=12)
plt.ylabel('angle [rad]',fontsize=12)
plt.grid(True)

# Subplot 4
ax4=fig.add_subplot(gs[2,2],facecolor=(0.9,0.9,0.9))
alpha2_funct,=ax4.plot([],[],'b',linewidth=2)
plt.xlim(t0,t_end)
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+0.1,np.pi),['0','π','2π','3π','4π','5π','6π'])
plt.xlabel('time [s]',fontsize=12)
plt.ylabel('angle [rad]',fontsize=12)
plt.grid(True)

ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()































########################################
