print("Slave, get your dignity back here!")
print("Slave, get your dignity back here!")
f=open("roof.csv","r")
data=f.read()

row233=data.split("\n")

we=row233[2]

us=row233[2].split(",")


roof_data=[]

for row in row233:
    roof_data.append(us[3])

print(roof_data[2])
    
