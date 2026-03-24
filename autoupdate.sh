#!/bin/bash
# Move into the project directory
cd ~/solar-data-3d-analytics

# Activate the virtual environment
source venv/bin/activate

# Execute the 3D rendering engine
python3 render_3d.py

# Push the updated chart to GitHub
git add index.html
git commit -m "auto: periodic 3D mesh update $(date)"
git push origin main
