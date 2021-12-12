import numpy as np
import matplotlib.pyplot as plt
import support_files_car as sfc
import animation_car as ac
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

# Create an object for the support functions.
support=sfc.SupportFilesCar()
constants=support.constants

# Load the constant values needed in the main file
Ts=constants[6]
outputs=constants[10] # number of outputs (psi, Y)
hz = constants[11] # horizon prediction period
x_dot=constants[12] # constant longitudinal velocity
time_length=constants[15] # duration of the manoeuvre

# Generate the refence signals
t=np.arange(0,time_length+Ts,Ts) # time from 0 to 10 seconds, sample time (Ts=0.1 second)
r=constants[13]
f=constants[14]
psi_ref,X_ref,Y_ref=support.trajectory_generator(t,r,f)
sim_length=len(t) # Number of control loop iterations
refSignals=np.zeros(len(X_ref)*outputs)

# Build up the reference signal vector:
# refSignal = [psi_ref_0, Y_ref_0, psi_ref_1, Y_ref_1, psi_ref_2, Y_ref_2, ... etc.]
k=0
for i in range(0,len(refSignals),outputs):
    refSignals[i]=psi_ref[k]
    refSignals[i+1]=Y_ref[k]
    k=k+1

# Load the initial states
y_dot=0
psi=0
psi_dot=0
Y=Y_ref[0]+10

states=np.array([y_dot,psi,psi_dot,Y])
statesTotal=np.zeros((len(t),len(states))) # It will keep track of all your states during the entire manoeuvre
statesTotal[0][0:len(states)]=states
psi_opt_total=np.zeros((len(t),hz))
Y_opt_total=np.zeros((len(t),hz))

# Load the initial input
U1=0 # Input at t = -1 s (steering wheel angle in rad (delta))
UTotal=np.zeros(len(t)) # To keep track all your inputs over time
UTotal[0]=U1

# To extract psi_opt from predicted x_aug_opt
C_psi_opt=np.zeros((hz,(len(states)+np.size(U1))*hz))
for i in range(1,hz+1):
    C_psi_opt[i-1][i+4*(i-1)]=1

# To extract Y_opt from predicted x_aug_opt
C_Y_opt=np.zeros((hz,(len(states)+np.size(U1))*hz))
for i in range(3,hz+3):
    C_Y_opt[i-3][i+4*(i-3)]=1

# Generate the discrete state space matrices
Ad,Bd,Cd,Dd=support.state_space()

# Generate the compact simplification matrices for the cost function
Hdb,Fdbt,Cdb,Adc=support.mpc_simplification(Ad,Bd,Cd,Dd,hz)

# Initiate the controller - simulation loops
k=0
for i in range(0,sim_length-1):

    # Generate the augmented current state and the reference vector
    x_aug_t=np.transpose([np.concatenate((states,[U1]),axis=0)])

    # From the refSignals vector, only extract the reference values from your [current sample (NOW) + Ts] to [NOW+horizon period (hz)]
    # Example: t_now is 3 seconds, hz = 15 samples, so from refSignals vectors, you move the elements to vector r:
    # r=[psi_ref_3.1, Y_ref_3.1, psi_ref_3.2, Y_ref_3.2, ... , psi_ref_4.5, Y_ref_4.5]
    # With each loop, it all shifts by 0.1 second because Ts=0.1 s
    k=k+outputs
    if k+outputs*hz<=len(refSignals):
        r=refSignals[k:k+outputs*hz]
    else:
        r=refSignals[k:len(refSignals)]
        hz=hz-1

    # Generate the compact simplification matrices for the cost function
    if hz<constants[11]: # Check if hz starts decreasing
        # These matrices (Hdb,Fdbt,Cdb,Adc) were created earlier at the beginning of the loop.
        # They constant almost throughout the entire simulation. However,
        # in the end of the simulation, the horizon period (hz) starts decreasing.
        # Therefore, the matrices need to be constantly updated in the end of the simulation.
        Hdb,Fdbt,Cdb,Adc=support.mpc_simplification(Ad,Bd,Cd,Dd,hz)

    ft=np.matmul(np.concatenate((np.transpose(x_aug_t)[0][0:len(x_aug_t)],r),axis=0),Fdbt)
    du=-np.matmul(np.linalg.inv(Hdb),np.transpose([ft]))
    x_aug_opt=np.matmul(Cdb,du)+np.matmul(Adc,x_aug_t)
    psi_opt=np.matmul(C_psi_opt[0:hz,0:(len(states)+np.size(U1))*hz],x_aug_opt)
    Y_opt=np.matmul(C_Y_opt[0:hz,0:(len(states)+np.size(U1))*hz],x_aug_opt)

    psi_opt=np.transpose((psi_opt))[0]
    psi_opt_total[i+1][0:hz]=psi_opt
    Y_opt=np.transpose((Y_opt))[0]
    Y_opt_total[i+1][0:hz]=Y_opt

    # Update the real inputs
    U1=U1+du[0][0]

    ######################### PID #############################################
    PID_switch=constants[17]

    if PID_switch==1:
        if i==0:
            e_int_pid_yaw=0
            e_int_pid_Y=0
        if i>0:
            e_pid_yaw_im1=psi_ref[i-1]-old_states[1]
            e_pid_yaw_i=psi_ref[i]-states[1]
            e_dot_pid_yaw=(e_pid_yaw_i-e_pid_yaw_im1)/Ts
            e_int_pid_yaw=e_int_pid_yaw+(e_pid_yaw_im1+e_pid_yaw_i)/2*Ts
            Kp_yaw=constants[18]
            Kd_yaw=constants[19]
            Ki_yaw=constants[20]
            U1_yaw=Kp_yaw*e_pid_yaw_i+Kd_yaw*e_dot_pid_yaw+Ki_yaw*e_int_pid_yaw

            e_pid_Y_im1=Y_ref[i-1]-old_states[3]
            e_pid_Y_i=Y_ref[i]-states[3]
            e_dot_pid_Y=(e_pid_Y_i-e_pid_Y_im1)/Ts
            e_int_pid_Y=e_int_pid_Y+(e_pid_Y_im1+e_pid_Y_i)/2*Ts
            Kp_Y=constants[21]
            Kd_Y=constants[22]
            Ki_Y=constants[23]
            U1_Y=Kp_Y*e_pid_Y_i+Kd_Y*e_dot_pid_Y+Ki_Y*e_int_pid_Y

            U1=U1_yaw+U1_Y


        old_states=states
    ######################### PID END #########################################

    # Establish the limits for the real inputs (max: pi/6 radians)

    if U1 < -np.pi/6:
        U1=-np.pi/6
    elif U1 > np.pi/6:
        U1=np.pi/6
    else:
        U1=U1

    # Keep track of your inputs as you go from t=0 --> t=7 seconds
    UTotal[i+1]=U1

    # Compute new states in the open loop system (interval: Ts/30)
    states=support.open_loop_new_states(states,U1)
    statesTotal[i+1][0:len(states)]=states

################################ ANIMATION LOOP ###############################

frame_amount=int(time_length/Ts)
lf=constants[4]
lr=constants[5]
lane_width=constants[16]
ac.vehicle_animation(t,statesTotal[:,3],statesTotal[:,1],UTotal,X_ref,Y_ref,psi_ref,frame_amount,lf,lr,lane_width)






#################
