import re
import sys

# define global dictionary
state = {}

# input is either from user input or command line (for testing)
def get_input(user_input_bool):
  if user_input_bool:
    return input("> ")
  else:
    return sys.argv[2]

# returns a list of tokens
def tokenise(inp):
  return inp.replace('(',' ( ').replace(')',' ) ').split()  # default split is any whitespace

# want to convert tokens to their appropriate types, can be integer or symbol (for now)
def read_token(t):
  if re.match('[-+]?[0-9]+\.[0-9]+', t):  # check if float
    return float(t)
  elif re.match("[-+]?[0-9]+", t):  # check if int
    return int(t)
  else:
    return t  # else a symbol is returned as a string exactly as it entered

# reads the list of tokens, and converts to parsed output list
def read_tokens(ts):
  token = ts.pop(0)  # read and remove first entry
  if token == '(':   # because the while loop calls read_tokens again it always checks for '('
    L = []
    while ts[0] != ')':
      L.append(read_tokens(ts))  # keep appending tokens until )
    ts.pop(0) # remove ending ')'
    return L  # when it returns, python remembers L in the 'outer' scope so this works (the next L = [] does not affect the outer scope L)
  else:  # else it's a token (str, float, int)
    return read_token(token)

# evaluates the parsed list of tokens
def eva(expr):
  # iterate over expr
  # if a list is found, call eval on that too
  v = 0  # initiate output value
  L = []
  try:
    e = expr.pop(0)  # if it's a list take & remove 1st element
  except:
    e = expr         # else it's a str or int so simply take it

  # basic maths operations
  if e == '+':
    for x in expr: v += eva(x)
    return v
  elif e == '*':
    v += 1  # for multiplication must initialise at 1 (not 0)
    for x in expr: v *= eva(x)
    return v
  elif e == '-':
    i = 0   # in Lisp we subtract everything from the first element
    for x in expr:
      i += 1
      if i == 1:
        v += eva(x)
      else:
        v -= eva(x)
    return v
  elif e == '/':
    i = 0   # in Lisp we divide everything from the first element
    for x in expr:
      i += 1
      if i == 1:
        v += eva(x)
      else:
        v /= eva(x)
    return v
  elif e == 'expt':
    v += pow(eva(expr[0]), eva(expr[1]))
    return v

  # equalities
  elif e == '=':   return eva(expr[0]) == eva(expr[1])
  elif e == '>':   return eva(expr[0]) >  eva(expr[1])
  elif e == '<':   return eva(expr[0]) <  eva(expr[1])
  elif e == '>=':  return eva(expr[0]) >= eva(expr[1])
  elif e == '<=':  return eva(expr[0]) <= eva(expr[1])
  elif e == 'T':   return True
  elif e == 'NIL': return False

  # other logic
  elif e == 'if':
    if eva(expr[0]): return eva(expr[1])
    else:            return eva(expr[2])

  # define variables and functions
  elif e == 'define':
    state[expr[0]] = eva(expr[1])  # define key:value pair for variable
  elif e == 'defun':
    state[expr[0]] = expr[1:]  # define key:value pair for function
  elif ( e in state.keys() ):  # check if key exists and return value
    if (type(state[e]) is list):     # if the value is a list, then treat as a function body
      args = state[e][0]
      body = state[e][1]
      k = 0
      y = body
      for i in args:
        y = [expr[k] if x==args[k] else x for x in y]  # replace variable names with real values
        k += 1
      return eva(y)
    else:                      # else it's a stored variable; return it
      return state[e] 
  # if it's not a defined symbol or statement just return
  else:
    return e
    
  
if sys.argv[1] == 'testing':
  user_input = False
elif sys.argv[1] == 'user_inp':
  user_input = True


# main loop: tokenise, parse, evaluate, print
while True:
  try:
    # input is either from user or command line (for testing)
    inp = get_input(user_input)
    # convert input to list of tokens
    ts = tokenise(inp)
    # "parse" tokens
    output = read_tokens(ts)
    # evaluate the parsed form, 'output' is a list
    final = eva(output)
    print(final)
  except EOFError: break
  if (not user_input): break

