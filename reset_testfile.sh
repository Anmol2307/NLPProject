cd NLP_v4
cp annotated_testbench ../NLP_V3/annotated_testbench
cp annotated_testbench ../NLP_v2_new/annotated_testbench
python3 convert_annotated_to_testfile.py
cd ../NLP_V3
python3 convert_annotated_to_testfile.py
cd ../NLP_v2_new
python3 convert_annotated_to_testfile.py
