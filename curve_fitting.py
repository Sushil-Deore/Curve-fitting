
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

# Curve fir for linear equation 
def func_linear(t,a,b):
	return a*t + b

#Curve fit for quadraric equation 

def func_quad(t,a,b,c):
	return a*pow(t,2) + b*t + c

# Curve fit for Cubic equation 

def func_cubic(t,a,b,c,d):
	return a*pow(t,3) + b*pow(t,2) + c*t + d

# Reading the thermodynamic data file

def read_file():
	temperature = []
	cp =[]

	for line in open('data','r'):
		values = line.split(',')
		temperature.append(float(values[0]))
		cp.append(float(values[1]))

	return[temperature, cp]

# Main program - Linear
temperature, cp = read_file()
popt,pcov = curve_fit(func_linear, temperature, cp)
fit_cp = func_linear(np.array(temperature), *popt)

plt.plot(temperature,cp, color="blue", linewidth=3)
plt.plot(temperature,fit_cp, color="red", linewidth=3)
plt.legend(['Actual Data', 'Curve Fit'])
plt.title('Specific Heat Vs. Temperature')
plt.xlabel('Temperature [K]')
plt.ylabel('Cp')
plt.show()

# Main program - Quadratic
temperature, cp = read_file()
popt,pcov = curve_fit(func_quad, temperature, cp)
fit_cp = func_quad(np.array(temperature), *popt)

plt.plot(temperature,cp, color="blue", linewidth=3)
plt.plot(temperature,fit_cp, color="red", linewidth=3)
plt.legend(['Actual Data', 'Curve Fit'])
plt.title('Specific Heat Vs. Temperature')
plt.xlabel('Temperature [K]')
plt.ylabel('Cp')
plt.show()

# Main program - Cubic
temperature, cp = read_file()
popt,pcov = curve_fit(func_cubic, temperature, cp)
fit_cp = func_cubic(np.array(temperature), *popt)

plt.plot(temperature,cp, color="blue", linewidth=3)
plt.plot(temperature,fit_cp, color="red", linewidth=3)
plt.legend(['Actual Data', 'Curve Fit'])
plt.title('Specific Heat Vs. Temperature')
plt.xlabel('Temperature [K]')
plt.ylabel('Cp')
plt.show()
