#Question: Draw the Pattern of N rows
"""
N=4
1
1   2
1   2   3
1   2   3   4
"""

N = int(input("Enter the Number of Rows: "))
for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
