#!/bin/bash
echo "AUTO EXECUTING<br/>"
python3 auto_execute.py
echo "ASPECT ANALYSING<br/>"
python3 aspect_analysis.py
echo "SENTIMENT ANALYSING<br/>"
python3 sentiment_analysis.py
echo "MOVING INTO PLOTTER<br/>"
cd ../plotter
echo "RUNNING PLOTTER UI<br/>"
python3 plotter_ui.py
echo "RUNNING CHROME<br/>"
google-chrome statistics.html	
echo "CHROME RUN"