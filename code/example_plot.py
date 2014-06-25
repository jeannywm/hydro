from datetime import datetime
datetime.strptime("2012-may-31 19:00", "%Y-%b-%d %H:%M")
datetime.datetime(2012, 5, 31, 19, 0)
#This is an example of how to plot data once you have an array of datetimes:

import matplotlib.pyplot as plt
import datetime
import numpy as np

x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
y = np.random.randint(100, size=x.shape)

plt.plot(x,y)
plt.show()
