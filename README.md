# python-lisp-interpreter

python v3.9.1+

To start the Lisp interpreter with user input from command line,

```python
python run.py 'user_inp'
```
Then you can perform actions e.g.
```
> (define r 3)
> (* r r)
> 9
```

or run tests in bash,

```
./tests.sh
```
The output of tests is:
```
Begin Test: (= 1 1)
True
Begin Test: (- 20 32 10)
-22.0
Begin Test: (/ 2.5 5.0 5.0)
0.1
Begin Test: (* 4 (* 2 3))
24.0
Begin Test: (/ 4 (/ 2 8.000))
16.0
Begin Test: (+ 10 (* 8 (+ 2 2)))
42.0
Begin Test: (if (> 10 20) (+ 1 1) (+ 3 3))
6.0
Begin Test: (if (T) (+ 1 1) (+ 3 3))
2.0
```
