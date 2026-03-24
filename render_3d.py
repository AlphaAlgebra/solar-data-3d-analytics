import plotly.graph_objects as go
# ... (Keep your data generation/z_grid code here) ...

# 1. CREATE the Figure first
fig = go.Figure(data=[go.Surface(
    z=z_grid, 
    colorscale='Rainbow'
)])

# 2. APPLY axis labels and main title
fig.update_layout(
    title='AlphaVisuals: Solar Data 3D Analytics',
    scene=dict(
        xaxis_title='Time (ms)',
        yaxis_title='Load (Ω)',
        zaxis_title='Voltage (V)'
    ),
    autosize=True
)

# 3. ADD the colorbar "legend" label
fig.update_traces(
    colorbar_title_text='Efficiency (%)',
    selector=dict(type='surface')
)

# 4. EXPORT to the web file
fig.write_html("index.html")
print("Optimization Complete: index.html generated.")
