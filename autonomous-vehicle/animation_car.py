import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


def vehicle_animation(t, y, psi, delta, xr, yr, psir, frame_amount, lf, lr, lane_width):
    def update_plot(num):
        car_determined.set_data(xr[0:num], y[0:num])

        car_1.set_data([xr[num]-lr*np.cos(psi[num]), xr[num]+lf*np.cos(psi[num])],
                       [y[num]-lr*np.sin(psi[num]), y[num]+lf*np.sin(psi[num])])

        car_1_body.set_data([0-lr*np.cos(psi[num]), 0+lf*np.cos(psi[num])],
                            [0-lr*np.sin(psi[num]), 0+lf*np.sin(psi[num])])

        car_1_body_extension.set_data([0, (lf+40)*np.cos(psi[num])],
                                      [0, (lf+40)*np.sin(psi[num])])

        car_1_back_wheel.set_data([-(lr+0.5)*np.cos(psi[num]), -(lr-0.5)*np.cos(psi[num])],
                                  [-(lr+0.5)*np.sin(psi[num]), -(lr-0.5)*np.sin(psi[num])])

        car_1_front_wheel.set_data([lf*np.cos(psi[num])-0.5*np.cos(psi[num]+delta[num]), lf*np.cos(psi[num])+0.5*np.cos(psi[num]+delta[num])],
                                   [lf*np.sin(psi[num])-0.5*np.sin(psi[num]+delta[num]), lf*np.sin(psi[num])+0.5*np.sin(psi[num]+delta[num])])

        car_1_front_wheel_extension.set_data([lf*np.cos(psi[num]), lf*np.cos(psi[num])+40*np.cos(psi[num]+delta[num])],
                                             [lf*np.sin(psi[num]), lf*np.sin(psi[num])+40*np.sin(psi[num]+delta[num])])

        yaw_angle_text.set_text(str(round(psi[num], 2))+' rad')
        steer_angle.set_text(str(round(delta[num], 2))+' rad')

        steering_wheel.set_data(t[0:num], delta[0:num])
        yaw_angle.set_data(t[0:num], psi[0:num])
        Y_position.set_data(t[0:num], y[0:num])

        return car_determined, car_1, car_1_body, car_1_body_extension,\
            car_1_back_wheel, car_1_front_wheel, car_1_front_wheel_extension,\
            yaw_angle_text, steer_angle, steering_wheel, yaw_angle, Y_position

    # Set up your figure properties
    fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
    gs = gridspec.GridSpec(3, 3)

    # Create a subplot for the motorcycle
    ax0 = fig.add_subplot(gs[0, :], facecolor=(0.9, 0.9, 0.9))
    plt.xlim(xr[0], xr[frame_amount])
    plt.ylabel('Y-distance [m]', fontsize=15)

    # Plot the lanes
    lane_1, = ax0.plot([xr[0], xr[frame_amount]], [
                       lane_width/2, lane_width/2], 'k', linewidth=0.2)
    lane_2, = ax0.plot([xr[0], xr[frame_amount]],
                       [-lane_width/2, -lane_width/2], 'k', linewidth=0.2)

    lane_3, = ax0.plot([xr[0], xr[frame_amount]], [
                       lane_width/2+lane_width, lane_width/2+lane_width], 'k', linewidth=0.2)
    lane_4, = ax0.plot([xr[0], xr[frame_amount]], [-lane_width /
                       2-lane_width, -lane_width/2-lane_width], 'k', linewidth=0.2)

    lane_5, = ax0.plot([xr[0], xr[frame_amount]], [
                       lane_width/2+2*lane_width, lane_width/2+2*lane_width], 'k', linewidth=3)
    lane_6, = ax0.plot([xr[0], xr[frame_amount]], [-lane_width /
                       2-2*lane_width, -lane_width/2-2*lane_width], 'k', linewidth=3)

    ref_trajectory = ax0.plot(xr, yr, 'b', linewidth=1)  # reference trajectory

    # Draw a motorcycle
    car_1, = ax0.plot([], [], 'k', linewidth=3)
    car_determined, = ax0.plot([], [], '-r', linewidth=1)

    # Create an object for the motorcycle (zoomed)
    ax1 = fig.add_subplot(gs[1, :], facecolor=(0.9, 0.9, 0.9))
    plt.xlim(-5, 30)
    plt.ylim(-4, 4)
    plt.ylabel('Y-distance [m]', fontsize=15)
    neutral_line = ax1.plot([-50, 50], [0, 0], 'k', linewidth=1)
    car_1_body, = ax1.plot([], [], 'k', linewidth=3)
    car_1_body_extension, = ax1.plot([], [], '--k', linewidth=1)
    car_1_back_wheel, = ax1.plot([], [], 'r', linewidth=4)
    car_1_front_wheel, = ax1.plot([], [], 'r', linewidth=4)
    car_1_front_wheel_extension, = ax1.plot([], [], '--r', linewidth=1)

    # Copyright
    copyright = ax0.text(0, 21, '© Nhat Vu', size=15)

    bbox_props_angle = dict(boxstyle='square', fc=(
        0.9, 0.9, 0.9), ec='k', lw='1')
    yaw_angle_text = ax1.text(25, 2, '', size='20',
                              color='k', bbox=bbox_props_angle)

    bbox_props_steer_angle = dict(
        boxstyle='square', fc=(0.9, 0.9, 0.9), ec='r', lw='1')
    steer_angle = ax1.text(25, -2.5, '', size='20',
                           color='r', bbox=bbox_props_steer_angle)

    # Create the function for the steering wheel
    ax2 = fig.add_subplot(gs[2, 0], facecolor=(0.9, 0.9, 0.9))
    steering_wheel, = ax2.plot(
        [], [], '-r', linewidth=1, label='steering angle [rad]')
    plt.xlim(0, t[-1])
    plt.ylim(np.min(delta)-0.1, np.max(delta)+0.1)
    plt.xlabel('time [s]', fontsize=15)
    plt.grid(True)
    plt.legend(loc='lower right', fontsize='small')

    # Create the function for the yaw angle
    ax3 = fig.add_subplot(gs[2, 1], facecolor=(0.9, 0.9, 0.9))
    yaw_angle_reference = ax3.plot(
        t, psir, '-b', linewidth=1, label='yaw reference [rad]')
    yaw_angle, = ax3.plot([], [], '-r', linewidth=1, label='yaw angle [rad]')
    plt.xlim(0, t[-1])
    plt.ylim(np.min(psi)-0.1, np.max(psi)+0.1)
    plt.xlabel('time [s]', fontsize=15)
    plt.grid(True)
    plt.legend(loc='lower right', fontsize='small')

    # Create the function for the Y-position
    ax4 = fig.add_subplot(gs[2, 2], facecolor=(0.9, 0.9, 0.9))
    Y_position_reference = ax4.plot(
        t, yr, '-b', linewidth=1, label='Y - reference [m]')
    Y_position, = ax4.plot([], [], '-r', linewidth=1, label='Y - position [m]')
    plt.xlim(0, t[-1])
    plt.ylim(np.min(y)-2, np.max(y)+2)
    plt.xlabel('time [s]', fontsize=15)
    plt.grid(True)
    plt.legend(loc='lower right', fontsize='small')

    car_ani = animation.FuncAnimation(fig, update_plot,
                                      frames=frame_amount, interval=20, repeat=True, blit=True)
    plt.show()

    return

    ###########################
