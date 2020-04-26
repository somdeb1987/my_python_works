def transform_time_to_temp(x1):
    x2= 2.0* x1
    return('%.5f' % x2)



import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)


n_points= 100



time_min = 0.
time_max = 60.



x_value = np.linspace(time_min, time_max, n_points, endpoint=True)
y_value = np.cos(2.*np.pi*x_value)



temp_tick_in_time_scale_value = [10.5, 30.6, 40.8]

temp_tick_value_in_temp_scale = [transform_time_to_temp(10.5),transform_time_to_temp (30.6),transform_time_to_temp(40.8)]


ax1.plot(x_value, y_value)

ax1.set_xlim(time_min, time_max)
ax1.set_xlabel("time_scale")
ax1.set_ylabel("variable")
ax1.grid(True)
ax2 = ax1.twiny()
ax2.set_xlabel("temperature  scale")
ax2.set_xlim(time_min, time_max)
ax2.set_xticks(temp_tick_in_time_scale_value)
ax2.set_xticklabels(temp_tick_value_in_temp_scale)

fig.savefig("myplot.png")
