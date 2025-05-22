import numpy as np
import plotly.graph_objs as go

def l0(x):
    return ((x-0.25)*(x-0.75)*(x-1.00)) / ((0-0.25)*(0-0.75)*(0-1.00))

def l1(x):
    return ((x-0)*(x-0.75)*(x-1.00)) / ((0.25-0)*(0.25-0.75)*(0.25-1.00))

def l2(x):
    return ((x-0)*(x-0.25)*(x-1.00)) / ((0.75-0)*(0.75-0.25)*(0.75-1.00))

def l3(x):
    return ((x-0)*(x-0.25)*(x-0.75)) / ((1.00-0)*(1.00-0.25)*(1.00-0.75))

x_points = np.array([0, 0.25, 0.75, 1.00])
y_points = np.array([2.0000, 2.2840, 3.1170, 3.7183])

def lagrange_poly(x, y):
    return l0(x)*y[0] + l1(x)*y[1] + l2(x)*y[2] + l3(x)*y[3]
print(lagrange_poly(0.50, y_points))

x_vals = np.linspace(min(x_points) - 1, max(x_points) + 1, 400)
y_vals = [lagrange_poly(x, y_points) for x in x_vals]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_vals, 
    y=y_vals, 
    mode='lines', 
    name='Lagrange Polynomial')
)

fig.add_trace(go.Scatter(
    x=x_points, 
    y=y_points, 
    mode='markers+text', 
    name='Data Points',
    text=[f'({x}, {y})' for x, y in zip(x_points, y_points)],
    textposition='top center')
)

fig.update_layout(
    title='Lagrange Interpolating Polynomial',
    xaxis_title='x',
    yaxis_title='P(x)',
    template='plotly_white'
)

fig.show()