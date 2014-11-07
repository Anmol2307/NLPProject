#!/bin/bash
./../stanford-parser-2012-11-12/lexparser.sh testfile.txt > stanford_out.txt
echo ""
echo "STARTING NLP ALGORITHM..."
echo ""
python2 nlp_algo.py
python2 sentiment_analyser.py
python2 prec_recall.py
cd plotter
python2 plotter_ui.py
echo ""
echo "...DONE"
