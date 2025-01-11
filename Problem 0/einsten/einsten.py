def iemcito(mass, c=pow(300000000, 2)):
    return mass * c


m = int(input("say the mass as a integer: "))
c = pow(300000000, 2)

print(f"E: {iemcito(m, c)}")
