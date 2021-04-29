import re
import sys

# Initialise some global variables
Lglobal = []  # list
#ts = [] # list of tokens

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
  if re.match('[-+]?[0-9]*\.?[0-9]+', t):  # check if float
    return float(t)
  elif re.match("[-+]?[0-9]+", t):  # check if int
    return int(t)
  else:
    return t  # else a symbol is returned as a string exactly as it entered

def read_tokens(ts):
  token = ts.pop(0)  # read and remove first entry
  if token == '(':   # because the while loop calls read_tokens again it always checks for '('
    L = []
    while ts[0] != ')':
      L.append(read_tokens(ts))  # keep appending tokens until )
    ts.pop(0) # remove ending ')'
    return L
  else:
    return read_token(token)

def eva(expr):
  # iterate over expr
  # if a list is found, call eval on that too
  # print(expr)
  v = 0
  try:
    e = expr.pop(0)  # if it's a list take & remove 1st element
  except:
    e = expr         # else it's a str or int so simply take
  if e == '+':
    v += eva(expr[0]) + eva(expr[1]); return v
  elif e == '-':
    v += eva(expr[0]) - eva(expr[1]); return v
  elif e == '*':
    v += eva(expr[0]) * eva(expr[1]); return v
  elif e == '/':
    v += eva(expr[0]) / eva(expr[1]); return v
  elif e == '>':
    return eva(expr[0]) > eva(expr[1])
  elif e == '<':
    return eva(expr[0]) < eva(expr[1])
  elif e == 'if':
    if eva(expr[0]):
      return eva(expr[1])
    else:
      return eva(expr[2])
  elif ( type(e) is list ):
    # print('it is a list')
    eva(e)
  else:       # if it's not a defined symbol or statement
    return e
    
  
if sys.argv[1] == 'testing':
  user_input = False
else:
  user_input = True

while True:
  try:
    inp = get_input(user_input)
    ts = tokenise(inp)
    # "parse" tokens into list(s)
    output = read_tokens(ts)
    # print('output: ', output)
    # evaluate, 'output' is a list
    val = eva(output)
    print(val)
    

  except EOFError: break
  if (not user_input): break




