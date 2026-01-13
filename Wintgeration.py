import numpy as np
def integrate(eqn,a,b):
    def f(x):
        return eval(eqn)
    def g(z):
        return f(( b - a ) / 2 * z + (b + a ) / 2)
        
    weight=[5/9,8/9,5/9]
    z=[-np.sqrt(3/5),0,np.sqrt(3/5)]
    sum=0
    
    for i in range(3):
         sum+=weight[i]*g(z[i])
    I=(b-a)/2 * sum 
    return I
if __name__ =="__main__":
    eqn=input("Enter the Equation : ")
    a=int(input("Enter the lower limit: "))
    b=int(input("Enter the upper limit: "))
    result=integrate(eqn,a,b)
    print(result)
