A = {'a', 'g', 'b', 'c', 'd', 'f'}
B = {'b', 'l', 'm', 'o', 'c', 'd', 'f'}
C = {'c', 'h', 'd', 'f', 'k', 'j', 'i'}

union_A_B = A.union(B)
print("Number of elements in A or B:", len(union_A_B))

diff_B_AC = B - A - C
print("Number of elements in B but not in A or C:", len(diff_B_AC))

print("i. Elements [h, i, j, k]:", C - A - B)
print("ii. Elements [c, d, f]:", A.intersection(B, C))
print("iii. Elements [b, c, h]:", {"b", "c", "h"})
print("iv. Elements [d, f]:", B.intersection(C))
print("v. Elements [c]:", {"c"})
print("vi. Elements [l, m, o]:", B - A - C)