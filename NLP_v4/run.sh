#!/bin/bash
python3 aspect_analyser.py
python3 sentiment_analyser.py
python3 prec_recall.py
cd plotter
python3 plotter_ui.py
<<<<<<< HEAD
python3 process_result_data.py
google-chrome statistics.html

=======
>>>>>>> d3039e5b38ff275a5fb785f40c3d356a2613c3dd
