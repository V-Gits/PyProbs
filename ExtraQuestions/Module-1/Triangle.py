from math import sqrt

A,B,C = map(int, input("Enter the Sides of Triangle: ").split(","))
Perimeter = (A+B+C)
S = Perimeter/2
Area =  sqrt(S*(S-A)*(S-B)*(S-C))
print(f"""
        Area of Triangle is {Area} sq units
        Perimeter of Triangle is {Perimeter} units
""")