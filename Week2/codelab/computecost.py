import numpy as np


def compute_cost(X, y, theta):
    # COMPUTECOST Compute cost for linear regression
    #   this function computes the cost of using theta as the
    #   parameter for linear regression to fit the data points in X and y

    # Initialize some useful values
    m = y.shape[0] # number of training examples

    # You need to return the following variables correctly 
    J = 0;

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta
    #               You should set J to the cost.

    
    J = (1/(2*m))*np.sum((np.dot(X,theta) - y)**2)

    

    # =========================================================================
    return J
    
