from z3 import *

x, y, a, t1, t2, t3, t4 = Ints(['x', 'y', 'a', 't1', 't2', 't3', 't4'])

solver = Solver()

def r(x, n):
  solver.add(x >= n)
  solver.add(x < n * 10)

r(x, 1000)
r(y, 10)
r(a, 100)
solver.add(t1 == a / 100 * y)
r(t1, 100)
solver.add(t1 % 10 == 6)
solver.add(t2 == x - t1 * 10)
r(t2, 100)
solver.add(t3 == ((a / 10) % 10) * y)
r(t3, 10)
solver.add(t4 / 10 == t2 - t3)
solver.add(t4 == (a % 10) * y)
solver.add(t4 % 10 == 0)
r(t4, 10)


r = solver.check()
if r == sat:
  m = solver.model()
  print(m[x], m[y], m[a], m[t1], m[t2], m[t3], m[t4])
else:
  print('unsat')

