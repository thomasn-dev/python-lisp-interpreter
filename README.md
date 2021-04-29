# python-lisp-interpreter

python v3.9.1+

## Description

An interpreter for Lisp written in python 3. It can interpret atoms or lists. A list is defined with parentheses (), for example,
```
(1 2 3)
```
is a list containing 1 2 3. Then aritmetic expressions can be used to evaluate a list, e.g.
```
> (+ 1 2 3)
> 6
```
or -, \*, / can be used. 
It can use floating numbers,
```
> (/ 10.0 4.0)
> 2.5 
```

There is an `if` statement like this,
```
> (if (2 > 1) (+ 3 3) (+ 1 1))
> 6
```
that is if 2 > 1 is true the (+ 3 3) will be evaluated, if the first expression is not true then (+ 1 1) will be evaluated.

You can `define` values like this,
```
> (define r 3)
> (+ r 1)
> 4
```
Or functions,
```
> (defun square (x) (* x x))
> (square 2)
> 4
> (defun mul3 (x y z) (* x y z))
> (mul3 2 3 4)
> 24
```

## Usage

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
Begin Test: abc
abc
Begin Test: (= 1 1)
True
Begin Test: (- 20 32 10)
-22
Begin Test: (/ 2.5 5.0 5.0)
0.1
Begin Test: (* 4 (* 2 3))
24
Begin Test: (/ 4 (/ 2 8.000))
16.0
Begin Test: (+ 10 (* 8 (+ 2 2)))
42
Begin Test: (expt 10 (+ 2 2))
10000
Begin Test: (if (> 10 20) (+ 1 1) (+ 3 3))
6
Begin Test: (if (T) (+ 1 1) (+ 3 3))
2
```
