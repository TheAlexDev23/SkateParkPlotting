import matplotlib.pyplot as plt
import numpy as np

# Precomputed values for optimization
WEIGHT = 60 * 9.8
RES_AIR_PRECOMP = 0.5 * 1.225 * 0.8 * 1.7

TIME_STEP = 0.04


def get_kinetic(x):
    return 2058 - ((0.875 * ((x - 2) ** 2)) * WEIGHT)


# Need to start slightly forward as the kinetic energy at displacement 0 is 0 and division by 0 cannot be computed
dis_y = 0.1
dis_y_arr = []

time = 0
vel = 0

while dis_y <= 2:
    kinetic = get_kinetic(dis_y)
    acc = kinetic / 60
    vel_tmp = vel
    vel_tmp += acc * TIME_STEP
    force = kinetic / vel_tmp + WEIGHT

    # Air resistance = 1/2 * air_density * drag_coeff * v² * surface area
    # RES_AIR_PRECOMP has average values for humans and earth
    res_air = RES_AIR_PRECOMP * (vel_tmp**2)
    # As the skate rolls the ground resistance is low
    res_ground = 0.2 * WEIGHT

    force -= res_air
    force -= res_ground

    acc = force / 60
    vel += acc * TIME_STEP

    dis_y += vel * TIME_STEP

    dis_y_arr.append(dis_y)

    print(f"At t:{time} d:{dis_y} k:{kinetic} a:{acc} v:{vel} f:{force}")

    time += TIME_STEP


dis_x_arr = np.arange(0, time, TIME_STEP)

plt.plot(dis_x_arr, dis_y_arr)
# plt.show()
plt.savefig("save.png")
