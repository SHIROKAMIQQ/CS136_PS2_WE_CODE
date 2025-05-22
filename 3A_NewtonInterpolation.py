import numpy as np
import plotly.graph_objs as go

a1 = (2.2840 - 2.0000) / (0.25 -  0)
a2 = (3.1170 - 2.2840) / (0.75 - 0.25)
a3 = (3.7183 - 3.1170) / (1.00 - 0.75)

b1 = (a2 - a1) / (0.75 - 0)
b2 = (a3 - a2) / (1.00 - 0.25)

c1 = (b2 - b1) / (1.00 - 0)

newton_coef = [2.00, a1, b1, c1]

x_points = np.array([0, 0.25, 0.75, 1.00])
y_points = np.array([2.00, 2.2840, 3.1170, 3.7183])

def newton_poly(x_data, coef, x):
    n = len(coef)
    result = coef[-1]
    for k in range(n - 2, -1, -1):
        result = result * (x - x_data[k]) + coef[k]
    return result

x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 400)
y_vals = [newton_poly(x_points, newton_coef, x) for x in x_vals]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_vals, 
    y=y_vals, 
    mode='lines', 
    name='Newton Polynomial')
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
    title='Newton Interpolating Polynomial',
    xaxis_title='x',
    yaxis_title='P(x)',
    template='plotly_white',
    showlegend=True
)
fig.show()
