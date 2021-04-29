#!/bin/bash

Test="(- 20 32)"
echo "Begin Test: $Test"
python3 run.py "$Test"

Test="(/ 2.500 5.000)"
echo "Begin Test: $Test"
python3 run.py "$Test"

Test="(+ 10 (* 8 (+ 2 2)))"
echo "Begin Test: $Test"
python3 run.py "$Test"

Test="(if (> 10 20) (+ 1 1) (+ 3 3))"
echo "Begin Test: $Test"
python3 run.py "$Test"