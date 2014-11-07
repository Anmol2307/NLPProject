#!/bin/bash
cd ../NLP_V3
./run.sh
cd ../NLP_v4
# python3 aspect_analyser.py
python3 sentiment_analyser_for_v3.py
python3 prec_recall_for_v3.py
cd plotter
python3 plotter_ui.py
python3 process_result_data.py
google-chrome statistics.html

