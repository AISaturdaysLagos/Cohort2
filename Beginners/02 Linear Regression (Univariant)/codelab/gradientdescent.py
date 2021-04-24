from computecost import compute_cost
import numpy as np

def gradient_descent(X, y, theta, alpha, num_iters):
    #GRADIENTDESCENT Performs gradient descent to learn theta
    #   this function updates theta by 
    #   taking num_iters gradient steps with learning rate alpha

    # Initialize some useful values
    m = y.shape[0] # number of training examples
    J_history = np.zeros([num_iters, 1]);

    for iter in range(num_iters):

        # ====================== YOUR CODE HERE ======================
        # Instructions: Perform a single gradient step on the parameter vector
        #               theta. 
        #
        # Hint: While debugging, it can be usefusl to print out the values
        #       of the cost function (compute_cost) and gradient here.
        #
        
        
        h_of_x = np.dot(X,theta)
        
        error_x = (alpha*(1/m))*np.sum((h_of_x-y).reshape(m,1)*X, axis = 0)
        
        theta = theta - error_x
        
        
        



        # ============================================================

        # Save the cost J in every iteration    
        J_history[iter] = compute_cost(X, y, theta);

    return theta, J_history



    
