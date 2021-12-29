"""Write a function to calculate area and circumference of a circle."""



PI=3.1415
def areaCircle(r):
    return PI*r*r
def circumferenceCircle(r):
    return 2*PI*r
r=(int(input("enter radius of circlr=")))
print("area=",'%.3f'%areaCircle(r))
print("circumference=",'%.3f'%circumferenceCircle(r))
