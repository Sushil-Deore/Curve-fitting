# Curve-fitting
The curve for specific heat as a function of temperature and it will be plotted and the plot will be compared with the actual plot. 
The specific heats at different temperature will be provided as inputs

Curve fitting can be defined as the process od constructing a curve or mathematical function that has the best fit to a series of data points subjects to constraints.

Initially, we will be introducing a program for linear, quadratic and cubic polynomial and check the results with the actual plot. 
Based on the results we are going to figure out the best possible ways to have a perfect fit.
We are using:
1.	popt :  It is an array with the optimal values for the parameters so that the sum of squared residuals od data is minimized.
2.	pcov : It is a 2-D array with the estimated covariance of the parameters in popt. It can be used to calculate the standard deviation error of popt.
3.	np.array(temperature) : This function stores the values of temperature in the form of array and passes it to the function numpy.
4.	*in*popt : It stores the values of the constant parameters(a,b,c) in the array popt.  

Result:

****Please check attached figure for understanding*****

From figures the curve fits better when the degree of the polynomial increases. 
It can be observed that the deviation of the curve fit with the actual data is more 
for linear equation and gradually the deviation decreases in the order of the polynomial. 
If we consider fourth, fifth order polynomial then the curve fir will overlap with the actual data.