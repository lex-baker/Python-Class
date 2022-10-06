import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, LineString;

p1 = Point(0,1)
p2  = Point(1,2)

plt.plot(p1.x, p1.y, 'bo')
plt.plot(p2.x, p2.y, 'bo')
plt.axis([0,2.5,0,2.5])
plt.grid(True)
plt.show()