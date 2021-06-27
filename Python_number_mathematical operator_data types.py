Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (0+1j)*(0+1J)
(-1+0j)
>>> 3.14j
3.14j
>>> 1j*(0+1j)
(-1+0j)
>>> 3+1j*3
(3+3j)
>>> (3+1j)*3
(9+3j)
>>> 1=1.5+0.5j
SyntaxError: cannot assign to literal
>>> a=1.5+0.5j
>>> a.real
1.5
>>> a=1=
SyntaxError: invalid syntax
>>> a=10
>>> type(a)
<class 'int'>
>>> a=10.9
>>> type(a)
<class 'float'>
>>> ceil(4.5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ceil(4.5)
NameError: name 'ceil' is not defined
>>> import math
>>> der(math)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    der(math)
NameError: name 'der' is not defined
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.log10(3)
0.47712125471966244
>>> math.pow(3,2)
9.0
>>> math.ciel(4.4)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    math.ciel(4.4)
AttributeError: module 'math' has no attribute 'ciel'
>>> mathceil(3.4)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mathceil(3.4)
NameError: name 'mathceil' is not defined
>>> math.ceil(3.4)
4
>>> math.floor(3.6)
3
>>> math.exp(3)
20.085536923187668
>>> math.sqrt(12)
3.4641016151377544
>>> int(math.sqrt(12))
3
>>> (10+2)>16
False
>>> ##mathematical operator
>>> 10%2
0
>>> 9 % 5
4
>>> 8 ** 2
64
>>> 9//2
4
>>> ##Comparison operator
>>> 8>3
True
>>> 3=!4
SyntaxError: invalid syntax
>>> 3!=4
True
>>> #logical operator
>>> if (10+6)> and 10%2 ==0:
	
SyntaxError: invalid syntax
>>> if (10+6)> and 10%2 ==0;
SyntaxError: invalid syntax
>>> if (10+6)> and 10%2 ==0:
	
SyntaxError: invalid syntax
>>> if (10+6)> 5 and 10%2 ==0:
	print("my condition is met")

	
my condition is met
>>> if (10+6)>55 and 10%2 ==0:
	print("my condition is met")

	
>>> (10+6)>55
False
>>> if (10+6)>55 or 10%2 ==0:
	print("my condition is met")

	
my condition is met
>>> a += 2
>>> 
>>> a=a+2
>>> a
14.9
>>> a=2
>>> a+=2
>>> a=a+2
>>> a
6
>>> a=2
>>> a=+2
>>> a
2
>>> a=a+2
>>> a
4
>>> foat('inf')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    foat('inf')
NameError: name 'foat' is not defined
>>> float('nan')
nan
>>> float('56+12')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float('56+12')
ValueError: could not convert string to float: '56+12'
>>> float('32'+'2')
322.0
>>> float('56'+'78')
5678.0
>>> (1>3)-(1<3)
-1
>>> 2**(3**2)
512
>>> (2**3)**2
64
>>> 2**3**2
512
>>> float(22//3+3/)
SyntaxError: invalid syntax
>>> float(22//3+3/3)
8.0
>>> float('inf')
inf
>>> #string
>>> name="Rohit"
>>> type(name)
<class 'str'>
>>> 