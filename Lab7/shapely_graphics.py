# Lex Baker
# Python For Scientists 
# Lab 7
# 10/4/22

from shapely.geometry import Polygon, Point, LineString, MultiPolygon
import matplotlib.pyplot as plt
from shapely.affinity import scale, translate, skew, rotate
from numpy import asarray

# functions from http://pydoc.net/Python/Shapely/1.2.13/shapely.examples.geoms/
def plot_point(g, o='bo', l='b'):
    plt.plot([g.x], [g.y], o, label=l)
def plot_line(g, o='r'):
    a = asarray(g)
    plt.plot(a[:,0], a[:,1], o)
def plot_polygon(g, o='r'):
    a = asarray(g.exterior)
    plt.fill(a[:,0], a[:,1], o, alpha=0.5)

"""
# creating a point, a line, and a polygon (a triangle)
triangle = Polygon([(0,0),(3,0),(0,4)]);
p1 = triangle.centroid;
x1 = LineString([(0,-1), (0,0)]);

# plotting all three of these shapes
plot_point(p1)
plot_polygon(triangle)
plot_line(x1)
plt.axis([-1,5,-1,5])
plt.show()
"""