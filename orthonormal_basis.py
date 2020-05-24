from z3 import *

# 1/sqrt(x1) * (x2, -x3, x4)
# 1/sqrt(x5) * (x6, 1, -x7)
# 1/sqrt(x8) * (x9, x10, x11)

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 = Ints(['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11'])

solver = Solver()
solver.add(x1 > 0);
solver.add(x1 < 10);
solver.add(x5 > 0);
solver.add(x5 < 10);
solver.add(x8 > 9);
solver.add(x8 < 100);
solver.add(x2 >= 0);
solver.add(x2 < 10);
solver.add(x3 > 0);
solver.add(x3 < 10);
solver.add(x4 >= 0);
solver.add(x4 < 10);
solver.add(x6 >= 0);
solver.add(x6 < 10);
solver.add(x7 > 0);
solver.add(x7 < 10);
solver.add(x9 >= 0);
solver.add(x9 < 10);
solver.add(x10 >= 0);
solver.add(x10 < 10);
solver.add(x11 >= 0);
solver.add(x11 < 10);
solver.add(x1 == x2*x2 + x3*x3 + x4*x4);
solver.add(x5 == x6*x6 + 1 + x7*x7);
solver.add(x8 == x9*x9 + x10*x10 + x11*x11);
solver.add(x2*x6 - x3 - x4*x7 == 0);
solver.add(x6*x9 + x10 - x7*x11 == 0);
solver.add(x9*x2 - x10*x3 + x11*x4 == 0);
solver.add(x1 % 4 != 0);
solver.add(x1 % 9 != 0);
solver.add(x5 % 4 != 0);
solver.add(x5 % 9 != 0);
solver.add(x8 % 4 != 0);
solver.add(x8 % 9 != 0);
solver.add(x8 % 25 != 0);
solver.add(x8 % 49 != 0);

r = solver.check()
if r == sat:
  m = solver.model()
  print(m[x1], m[x2], m[x3], m[x4], m[x5], m[x6], m[x7], m[x8], m[x9], m[x10], m[x11])
else:
  print('unsat')

