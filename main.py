import matplotlib.pyplot as plt
import numpy as np

MASS = 60
GRAVITY = 9.8

# Precomputed values for optimization
WEIGHT = MASS * GRAVITY
VEL_PRECOMP = 2 / MASS
RES_AIR_PRECOMP = 0.5 * 1.225 * 0.8 * 1.7


TIME_STEP = 0.01


def get_kinetic(x):
    return 2058 - ((0.875 * ((x - 2) ** 2)) * WEIGHT)

# Need to start slightly forward as the kinetic energy at displacement 0 is 0 and division by 0 cannot be computed
dis_y = 0.1
dis_y_arr = []

time = 0
vel = 0

next_kinetic = get_kinetic(dis_y)

iterations = 0

while dis_y <= 2:
    prev_dis = dis_y

    vel_new = np.sqrt(VEL_PRECOMP * next_kinetic)
    acc = (vel_new - vel)/TIME_STEP
    force = acc * MASS

    # Air resistance = 1/2 * air_density * drag_coeff * v² * surface area
    # RES_AIR_PRECOMP has average values for humans and earth
    res_air = RES_AIR_PRECOMP * (vel_new**2)
    # As the skate rolls the ground resistance is low
    res_ground = 0.2 * WEIGHT
    
    resistance_force = 0
    resistance_force -= res_air
    resistance_force -= res_ground

    force -= resistance_force

    acc = force / MASS
    vel += acc * TIME_STEP
    dis_y += vel * TIME_STEP

    print(f"At t:{time} d:{dis_y} k:{next_kinetic} a:{acc} v:{vel} f:{force}")

    resistance_work = resistance_force * (dis_y - prev_dis)
    next_kinetic = get_kinetic(dis_y) - resistance_work

    dis_y_arr.append(dis_y)
    time += TIME_STEP
    iterations += 1


# dis_x_arr = np.arange(0, time, TIME_STEP)
prev_x = 0
dis_x_arr = [prev_x]

for i in range(iterations - 1):
    prev_x += TIME_STEP
    dis_x_arr.append(prev_x)

plt.plot(dis_x_arr, dis_y_arr)
# plt.show()
plt.savefig("save2.png")
