from math import pi

def cylinder_volume(r, h):
    """Returns the volume of a cylinder given a radius (r) and height (h)."""
    if r < 0 or h < 0:
        volume = "None"
    else:
        volume = pi*r*r*h
    return volume

def torus_volume(r,R):
    """Returns the volume of a torus given a minor radius (r) and major radius (R)."""
    if R < 0 or r < 0:
        volume = "None"
    else:
        '''From google search.'''
        volume = (pi * r ** 2) * (2 * pi * R)
    return volume

if __name__ == '__main__':


    r = 3
    h = 5
    cylVol = cylinder_volume(r, h)
    print("Radius:", r)
    print("Height:", h)
    print("Cylinder Volume:", cylVol)

    R = 3.5
    r = 0.5
    torusVol = torus_volume(r, R)
    print("Radius:", r)
    print("Height:", h)
    print("Torus Volume:", torusVol)