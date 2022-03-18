import numpy as np
Touched by user2

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)

for i in range(4):
    y[i, :] = x[i, :] + v #i는 가로줄의 번호(첫번째줄...등)등/ :는 모든값을 나타냄

#   1 2 3
#   4 5 6
#   7 8 9
#   10 11 12(x)

# + 1 0 1(v)

#   2 2 4
#   5 5 7
#   8 8 10
#   11 11 13

print(y)
 
