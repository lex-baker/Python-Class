def areaPerimeter(width=2,height=3):
	return (width*height, 2 * (width+height))

a,p = areaPerimeter(2,3)
print("The area is", a, "and the perimeter is", p)

a2, p2 = areaPerimeter(2)
print("The area is still", a2, "and the perimeter is still", p2)

a3, p3 = areaPerimeter()
print("Even now, the area is still", a2, "and the perimeter is still", p2)