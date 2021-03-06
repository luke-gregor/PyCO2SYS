import numpy as np
from matplotlib import pyplot as plt
from PyCO2SYS import CO2SYS

# Define input conditions
dic = np.linspace(1600, 3200, 1000)
ta = 2250
tmp = 25
sal = 35
prs = 0
si = 0
phos = 0

# Run CO2SYS
cdict = CO2SYS(ta, dic, 1, 2, sal, tmp, tmp, prs, prs, si, phos, 3, 10, 3)

# Recreate ESM10 Fig. 2
fvars = ['gammaTCin', 'gammaTAin', 'betaTCin', 'betaTAin', 'omegaTCin',
         'omegaTAin']
fmults = [1, -1, 1, -1, -1, 1]
fclrs = ['#453c90', '#b84690', '#b84690', '#007831', '#df0023', '#40b4b6']
flabels = ['$\\gamma_\mathrm{DIC}$', '$-\\gamma_\mathrm{Alk}$',
           '$\\beta_\mathrm{DIC}$', '$-\\beta_\mathrm{Alk}$',
           '$-\\omega_\mathrm{DIC}$', '$\\omega_\mathrm{Alk}$']
fig, ax = plt.subplots()
for i, fvar in enumerate(fvars):
    ax.plot(dic*1e-3, cdict[fvar]*fmults[i]*1e3, c=fclrs[i], label=flabels[i])
ax.legend(edgecolor='k')
ax.set_xlim([1.6, 3.2])
ax.set_ylim([0.1, 1.0])
ax.set_title('Buffer factors at Alk = {} mM'.format(ta*1e-3))
ax.set_xlabel('DIC (mM)')
ax.set_ylabel('buffer factor (mM)')
ax.grid(alpha=0.4)
