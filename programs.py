'''for letter in "ABCDEFGHIJKLMNOUPQRSTUVWXYZ":
	if letter in "AEIOU":
		print(letter, "is a vowel")
	else:
		print(letter, "is not a vowel")'''


'''i=1
while i<6:
    print(i)
    i += 1'''


'''count = 0
while (count < 9):
   print("The count is:", count)
   count+=1
print("Good bye!")'''


'''import sys
def print_unicode_table(word):
    word = None
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
             print("usage: {0} [string]".format(sys.argv[0]))
             word = 0
        else:
            word = sys.argv[1].lower()
    if word != 0:
          print_unicode_table(word)



Modify quadratic.py so that 0.0 factors are not output,and so that negative
factors are output as - n rather than as + -n. This involves replacing the
last five lines with about fifteen lines. A solution is provided in quadratic_
ans.py. (Windows and cross-platform users should modify quadratic_
uni.py; a solution is provided in quadratic_uni_ans.py.)


from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
----------------------------------------
import cmath
import math
import sys
def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                 print("zero is not allowed")
                 x = None
        except ValueError as err:
             print(err)
    return x
print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
         root = math.sqrt(discriminant)
    else: # discriminant < 0
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
equation = ("{0}x\N{SUPERSCRIPT TWO} + {1}x + {2} = 0"
" \N{RIGHTWARDS ARROW} x = {3}").format(a, b, c, x1)
equation="{0}x{1}".format(a,2)
if b!=0:
    if(b<0):
        equation+="-{0}x".format(abs(b))
    else:
        equation+="+{0}x".format(b)
if c!=0:
    if(c<0):
        equation+="-{0}x".format(abs(c))
    else:
        equation+="+{0}x".format(c)
if x2 is not None:
     equation += " or x = {0}".format(x2)
print(equation)

equation = ("{a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0"
" \N{RIGHTWARDS ARROW} x = {x1}").format(**locals())

equation = ("{}x\N{SUPERSCRIPT TWO} + {}x + {} = 0"
" \N{RIGHTWARDS ARROW} x = {}").format(a, b, c, x1)
'''
-----------------------------------------------------
'''"COUNTRY","2000","2001",2002,2003,2004
"ANTIGUA AND BARBUDA",0,0,0,0,0
"ARGENTINA",37,35,33,36,39
"BAHAMAS, THE",1,1,1,1,1
"BAHRAIN",5,6,6,6,6

<table border='1'><tr bgcolor='lightgreen'>
<td>Country</td><td align='right'>2000</td><td align='right'>2001</td>
<td align='right'>2002</td><td align='right'>2003</td>
<td align='right'>2004</td></tr>
...
<tr bgcolor='lightyellow'><td>Argentina</td>
<td align='right'>37</td><td align='right'>35</td>
<td align='right'>33</td><td align='right'>36</td>
<td align='right'>39</td></tr>
...
</table>'''


import matplotlib.pyplot as plt
from matplotlib import colors #as mcolors
import xml.sax.saxutils
def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"

            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
             break
    print_end()
def print_start():
    print("<table border='1'>")
def print_end():
    print("</table>")
   
def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                     field = escape_html(field)
                else:
                     field = "{0} ...".format(
                              escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
print("</tr>")
def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                 quote = c
            elif quote == c: # end of quoted string
                quote = None
            else:
                 field += c # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
             fields.append(field)
             field = ""
        else:
             field += c # accumulating a field
    if field:
         fields.append(field) # adding the last field
    return fields

def escape():
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text 
'''def xml.:
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        return text '''

