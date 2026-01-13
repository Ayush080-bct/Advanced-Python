import module as m
principal=int(input("Enter the principal amount:"))
Year=int(input("Enter the years:"))
Rate=int(input("Entere the rate: "))
print(f"simplr interest:{m.simpleinterest(principal,Year,Rate)}")
print(f"Compound interest:{m.compoundinterest(principal,Year,Rate)}")