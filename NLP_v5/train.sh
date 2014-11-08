#!/bin/bash
echo "Starting Bag Of Words"
python3 create_bag_of_words.py
echo "Starting Senti Bag Of Words"
python3 create_senti_bag_of_words.py
echo "Starting Trainer"
python3 trainer.py