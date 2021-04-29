#!/bin/bash

Test="(= 1 1)"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(- 20 32 10)"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(/ 2.5 5.0 5.0)"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(* 4 (* 2 3))"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(/ 4 (/ 2 8.000))"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(+ 10 (* 8 (+ 2 2)))"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(if (> 10 20) (+ 1 1) (+ 3 3))"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"

Test="(if (T) (+ 1 1) (+ 3 3))"
echo "Begin Test: $Test"
python3 run.py 'testing' "$Test"
