#!/bin/bash
python3 aspect_analyser.py
python3 sentiment_analyser.py
python3 prec_recall.py
cd plotter
python3 plotter_ui.py