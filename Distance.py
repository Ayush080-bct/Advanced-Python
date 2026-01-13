#WaP to create a class Distance which has feet and inches as data memeber .overload any two operator
class Distance:
    def __init__(self,feet,inch):#constructor,self is like this of c++ which point to current obj
        self.feet=feet
        self.inch=inch
    def __str__(self):
        return f"{self.feet} feet {self.inch} inch"
    def __add__(self,other):
        i=self.inch+other.inch
        if i>12:
            I=i%12
            i=i//12# / produce float
            f=self.feet+other.feet+i
        return Distance(f,I)
    def __sub__(self,other):
        return Distance(self.feet-other.feet,self.inch-other.inch)
            
d1=Distance(5,9)
d2=Distance(4,5)
d3=d1+d2
d4=d1-d2
print(d3)
print(d4)

    

