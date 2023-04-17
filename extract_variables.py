import matplotlib.pyplot as plot
fig = plot.figure()
ax = fig.add_axes([0,0,1,1])
Color = ['Brown', 'Yellow', 'Red', 'Orange', 'Blue', 'Green']
Frequency = [12,10,9,6,3,5]
plot.title('Bar Graph for M&M colour')
plot.xlabel('Color')
plot.ylabel('Frequency')
ax.bar(Color,Frequency)
plot.show() 