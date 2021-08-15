import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

x = np.linspace(-2,2,1000)
plt.plot(x,norm.pdf(x,0,1))
plt.show()

# probability that x < 0
norm.cdf(0,0,1)

norm.cdf(1,0,1) - norm.cdf(-1,0,1)

# this shows that the variable is within the CDF guidelines