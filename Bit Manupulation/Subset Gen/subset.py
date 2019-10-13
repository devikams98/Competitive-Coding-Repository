

def subSet(a, n):
    pn = 1 << n
    print(pn)
    for i in range(pn):
        for j in range(n):
            if (1 << j) & i:
                print(a[j], end='')

        print()


n = int(input())  # Example 5

a = []
for i in range(n):
    a.append(int(input()))
subSet(a, n)
'''Example
Input : 5
10           
15
20
25
30
Output:
32

10
15
1015
20
1020
1520
101520
25
1025
1525
101525
2025
102025
152025
10152025
30
1030
1530
101530
2030
102030
152030
10152030
2530
102530
152530
10152530
202530
10202530
15202530
1015202530
'''
