import matplotlib.pyplot as plt
dict={"java":22.2,"python":17.6,"PHP":8.8,"C#":8,"C++":6.7}
x=dict.keys()
y=dict.values()
fig=plt.figure(figsize=(6,4))
plt.bar(x,y,color="teal",width=0.5)
plt.title("popularity of programing language")
plt.xlabel("pg")
plt.ylabel("popularity")
plt.show()