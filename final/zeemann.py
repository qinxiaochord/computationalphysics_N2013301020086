import numpy as np
import matplotlib.pyplot as plb

db = 0.1
b = np.arange(0, 10, db)
E2 = 3. / 4. + b / 2.
E_2 = 3. / 4. - b / 2.
E11 = - 1. / 4. + np.sqrt(3. / 4. + 1. / 4. * (1 + b)**2)
E12 = - 1. / 4. - np.sqrt(3. / 4. + 1. / 4. * (1 + b)**2)
E_11 = - 1. / 4. + np.sqrt(3. / 4. + 1. / 4. * (1 - b)**2)
E_12 = - 1. / 4. - np.sqrt(3. / 4. + 1. / 4. * (1 - b)**2)
E01 = - 1. / 4. + np.sqrt(1 + b**2 / 4.)
E02 = - 1. / 4. - np.sqrt(1 + b**2 / 4.)

plb.figure(figsize = (8,4))
ax = plb.axes(xlim = (0, 10), ylim = (-6, 6))
plb.plot(b, E2, linestyle = '-', linewidth = 1.0, color = 'b', label = '$m_I+m_J = +2$')
plb.plot(b, E_2, linestyle = '-', linewidth = 1.0, color = 'k', label = '$m_I+m_J = -2$')
plb.plot(b, E11, linestyle = '-', linewidth = 1.0, color = 'g', label = '$m_I+m_J = +1$')
plb.plot(b, E12, linestyle = '-', linewidth = 1.0, color = 'g')
plb.plot(b, E_11, linestyle = '-', linewidth = 1.0, color = 'r', label = '$m_I+m_J = -1$')
plb.plot(b, E_12, linestyle = '-', linewidth = 1.0, color = 'r')
plb.plot(b, E01, linestyle = '-', linewidth = 1.0, color = 'y', label = '$m_I+m_J = 0$')
plb.plot(b, E02, linestyle = '-', linewidth = 1.0, color = 'y')
plb.title('Energy changes with b varying.')
plb.xlabel = ('$b$')
plb.ylabel = ('$\frac{E}{A}$')
plb.legend(loc = 'upper right')
plb.show()
