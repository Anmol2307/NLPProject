#!/bin/bash
./../stanford-parser-2012-11-12/lexparser.sh testfile.txt > stanford_out.txt
echo ""
echo "STARTING NLP ALGORITHM..."
echo ""
python2 nlp_algo.py
echo ""
echo "...DONE"