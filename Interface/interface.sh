#!/bin/bash

python3 interface.py
python3 aspect_analysis.py
python3 sentiment_analysis.py
cd ../plotter
python3 plotter_ui.py
google-chrome statistics.html	