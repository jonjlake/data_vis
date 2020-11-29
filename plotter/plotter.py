import matplotlib.pyplot as plt

fig, ax = plt.subplots()

plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel('some numbers')
plt.show()

#plt.savefig('plot.jpg')
fig.savefig('plot.jpg')
