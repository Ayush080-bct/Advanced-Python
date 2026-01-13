def simpleinterest(p,t,r):
    return p*t*r*0.01
def compoundinterest(p,t,r):
    return ((1+r/100)**t-1)*p
if __name__=="__main__":
    print(simpleinterest(4000,3,5))
    print(compoundinterest(4000,3,5))
