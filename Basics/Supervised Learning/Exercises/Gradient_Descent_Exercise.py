import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math

def predict_using_sklearn():
    df= pd.read_csv('/home/arghanath/Documents/Machine Learning/Resources Folder/ML/3_gradient_descent/Exercise/test_scores.csv')
    r=LinearRegression()
    r.fit(df[['math']],df.cs)
    return r.coef_, r.intercept_

def gradient_descent_exercise(x,y):
    m_curr=b_curr=0
    iterations=1000
    n=len(x)
    learning_rate=0.002
    cost_previous=0

    for i in range(iterations):
        y_predicted= m_curr * x + b_curr
        cost=(1/n) * sum([val**2 for val in (y- y_predicted)])
        md= -(2/n)*sum(x * (y- y_predicted))
        bd= -(2/n) * sum(y-y_predicted)
        m_curr= m_curr + learning_rate * md
        b_curr= b_curr + learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous=cost
        print("m {} b{} cost{} iteration {}".format(m_curr, b_curr, cost,i))
    return m_curr, b_curr

if __name__=='main':
    df=pd.read_csv('/home/arghanath/Documents/Machine Learning/Resources Folder/ML/3_gradient_descent/Exercise/test_scores.csv')
    x=np.array(df.math)
    y=np.array(df.cs)

    m,b = gradient_descent_exercise(x,y)
    print("Using gradient descent function: Coef {} Intercept {}".format(m, b))

    m_sklearn, b_sklearn= predict_using_sklearn()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))