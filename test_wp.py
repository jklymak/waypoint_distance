import numpy as np
import matplotlib.pyplot as plt
import waypoint_distance as wd


wplons = [-127.5, -127.2, -127.1, -127]
wplats = [44.5, 45, 44.7, 44.3]

ts = [0, 1, 2, 3]
time = np.linspace(0, 3, 20)
shiplons = np.interp(time, ts, wplons) + np.random.randn(len(time)) * 0.01
shiplats = np.interp(time, ts, wplats) + np.random.randn(len(time)) * 0.01

alongx, acrossx, segment = wd.get_simple_distance(shiplons, shiplats, wplons, wplats)
wpalong, wpacross, wpsegment = wd.get_simple_distance(wplons, wplats, wplons, wplats)

fig, ax = plt.subplots()
ax.plot(wplons, wplats)

ax.plot(shiplons, shiplats, '.')
for ind in range(len(wpalong)):
    ax.text(wplons[ind], wplats[ind], f'{wpalong[ind]/1000:1.1f}', fontsize=6)
for ind in range(len(shiplons)):
    ax.text(shiplons[ind], shiplats[ind], f'{alongx[ind]/1000:1.1f}', fontsize=6, color='C1')

plt.show()


