from z3 import *

s = Solver()
a = [[Int("a_%s_%s" % (i, j)) for j in range(5)] for i in range(3)]

for i in range(3):
  for j in range(5):
    if i - 1 >= 0:
      s.add(a[i][j] != a[i-1][j])
    if j + 1 <= 4:
      s.add(a[i][j] != a[i][j+1])
    if i + 1 <= 2:
      s.add(a[i][j] != a[i+1][j])
    if j - 1 >= 0:
      s.add(a[i][j] != a[i][j-1])
    if i - 1 >= 0 and j - 1 >= 0:
      s.add(a[i][j] == a[i-1][j-1])
    if i + 1 <= 2 and j + 1 <= 4:
      s.add(a[i][j] == a[i+1][j+1])
    s.add(Or(a[i][j] == 2, a[i][j] == 3, a[i][j] == 5))
    s.add(a[0][0] * a[0][4] * a[2][0] * a[2][4] == 3 * 2 * 2 * 5)
    s.add(a[0][1] * a[0][2] * a[0][3] * a[1][0] * a[1][4] * a[2][1] * a[2][2] * a[2][3] == 5 * 2 * 5 * 3 * 5 * 3 * 2 * 2)
    s.add(a[1][1] * a[1][2] * a[1][3] == 3 * 3 * 2 or a[1][1] * a[1][2] * a[1][3] == 3 * 3 * 5 or a[1][1] * a[1][2] * a[1][3] == 2 * 3 * 5)

if s.check() == sat:
  m = s.model()
  print(m)
else:
  print("failed to solve")
