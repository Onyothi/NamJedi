from numpy import * 
from pylab import *

B = 0.025	# the magnetic field
p = 2.5		# the electron energy index
l = 1.0e4	# this is the length of emission region
kappa = 1.0e7	# the normalizer

nu = linspace(1.0e12,1.0e18,10)

J = kappa*(B**((p+1)/2)) * (nu**(-(p-1)/2)) # emissivity
I = (J*l)/(4*pi) # intensity
I_nu = I*nu
data = [nu, I]
print data

# Plotting the SED
plot(log10(nu),log10(I_nu), 'o-')
title('Rough SED estimate')
xlabel('frequency')
ylabel('intensity')
savefig('roughEstimate.jpg')
show()
