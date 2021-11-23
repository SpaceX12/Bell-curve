import pandas as pa
import plotly.figure_factory as ff

data = pa.read_csv('data.csv')

m = data['Avg Rating'].tolist()

plot = ff.create_distplot([m], ['Average Smartphone Company Rating'], show_hist= False)
plot.show()