import numpy as np



def gradient_descent(x,y):
    m_curr=b_curr=0
    rate=0.0002
    n=len(x)
    iterations=10000
    for i in range(iterations):

        y_predicted=m_curr * x + b_curr
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        print("m = {} , b = {} , cost = {}".format(m_curr,b_curr,cost))
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)* sum(y-y_predicted)
        m_curr=m_curr - rate*md
        b_curr=b_curr - rate*bd


x=np.array([92,56,88,70,80,49,65,35,66,67])
y=np.array([98,68,81,80,83,52,66,30,68,73])
gradient_descent(x,y)