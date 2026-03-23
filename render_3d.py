import numpy as np
import plotly.graph_objects as go

# 1. Generate high-fidelity 3D rainbow mesh data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x_grid, y_grid = np.meshgrid(x, y)
z_grid = np.sin(np.sqrt(x_grid**2 + y_grid**2))

# 2. Build the Surface Plot with Rainbow Colorscale
fig = go.Figure(data=[go.Surface(
    z=z_grid, 
    colorscale='Rainbow',
    colorbar_title='Voltage (V)'
)])

# 3. Apply Professional Styling
fig.update_layout(
    title='AlphaVisuals: Solar Data 3D Analytics',
    scene=dict(
        xaxis_title='Time (ms)',
        yaxis_title='Load (Ω)',
        zaxis_title='Voltage (V)'
    ),
    autosize=True
)

# 4. Export to HTML for your Portfolio
fig.write_html("index.html")
print("Optimization Complete: index.html generated.")
