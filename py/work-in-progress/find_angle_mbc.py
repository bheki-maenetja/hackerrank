# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import asin, pi, degrees

def find_angle(ab, bc):
    mc = 0.5 * (pow(ab, 2) + pow(bc, 2)) ** 0.5
    mcb = asin(ab / 2 * mc)
    print(degrees(asin(mc / bc)))
    return round((asin(mc / bc) / pi) * 180)

if __name__ == "__main__":
    angle = find_angle(int(input()), int(input()))
    print(str(angle) + u"\N{DEGREE SIGN}")
