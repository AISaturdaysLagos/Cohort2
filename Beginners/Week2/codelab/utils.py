import numpy as np



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def checkCost(J):
    color = ""
    exp = 32.07
    if(abs(J-exp) > 0.005):
        color = bcolors.FAIL
    else:
        color = bcolors.OKGREEN


    print('With theta = [0 ; 0]\nCost computed =',color,J,'\n',bcolors.ENDC);
    print('Expected cost value (approx)',color,32.07,'\n',bcolors.ENDC);
    
    return color

def furtherCheckCost(J, color):
    print('\nWith theta = [-1 ; 2]\nCost computed =',color,J, bcolors.ENDC);
    print('Expected cost value (approx)',color,54.24,bcolors.ENDC);

    
    
def checkGradientDescent(theta, J_history):
    exp = [-3.6303, 1.1664]
    res = [ float('%.4f' % elem) for elem in theta.tolist() ]
    
    color = ''
    if(exp == res):
        color = bcolors.OKGREEN
    else:
        color = bcolors.FAIL

    # print theta to screen
    print('Theta found by gradient descent:');
    print(color, res, bcolors.ENDC);
    print('Expected theta values (approx)\n');
    print(color,'[-3.6303, 1.1664]', bcolors.ENDC);
    
    return color